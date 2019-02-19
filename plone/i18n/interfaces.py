# -*- coding: utf-8 -*-
from zope.interface import Attribute
from zope.interface import Interface
from zope import schema
from plone.supermodel import model
# Definition of Import PloneMessageFactory to create messages in the plone
# domain. We do a fresh re-definition here as to break the dependency on
# `Products.CMFPlone.PloneMessageFactory`.
from zope.i18nmessageid import MessageFactory
_ = PloneMessageFactory = MessageFactory('plone')


class ILanguageUtility(Interface):
    """Marker interface for the portal_languages tool.
    """


class INegotiateLanguage(Interface):
    """Result of language negotiation
    """

    language = Attribute('Language to use')
    default_language = Attribute('Default language')
    language_list = Attribute('List of language preferences in order')


class ILanguageSchema(Interface):
    model.fieldset(
        'general',
        label=_(u'General'),
        fields=[
            'default_language',
            'available_languages',
            'use_combined_language_codes',
            'display_flags',
            'always_show_selector'
        ],
    )

    default_language = schema.Choice(
        title=_(u'heading_site_language', default=u'Site language'),
        description=_(
            u'description_site_language',
            default=u'The language used for the content and the UI of '
                    u'this site.'
        ),
        default='en',
        required=True,
        vocabulary='plone.app.vocabularies.AvailableContentLanguages'
    )

    available_languages = schema.List(
        title=_(u'heading_available_languages',
                default=u'Available languages'),
        description=_(u'description_available_languages',
                      default=u'The languages in which the site should be '
                              u'translatable.'),
        required=True,
        default=['en'],
        missing_value=[],
        value_type=schema.Choice(
            vocabulary='plone.app.vocabularies.AvailableContentLanguages'
        )
    )

    use_combined_language_codes = schema.Bool(
        title=_(
            u'label_allow_combined_language_codes',
            default=u'Show country-specific language variants'
        ),
        description=_(
            u'help_allow_combined_language_codes',
            default=u'Examples: pt-br (Brazilian Portuguese), '
                    u'en-us (American English) etc.'
        ),
        default=True,
        required=False
    )

    display_flags = schema.Bool(
        title=_(
            u'label_display_flags',
            default=u'Show language flags'
        ),
        description=u'',
        default=False,
        required=False
    )

    always_show_selector = schema.Bool(
        title=_(
            u'label_always_show_selector',
            default=u'Always show language selector'
        ),
        description=u'',
        default=False,
        required=False
    )

    model.fieldset(
        'negotiation_scheme',
        label=_(u'Negotiation scheme', default=u'Negotiation scheme'),
        fields=[
            'use_content_negotiation',
            'use_path_negotiation',
            'use_cookie_negotiation',
            'authenticated_users_only',
            'set_cookie_always',
            'use_subdomain_negotiation',
            'use_cctld_negotiation',
            'use_request_negotiation',
        ],
    )
    use_content_negotiation = schema.Bool(
        title=_(u'heading_language_of_the_content',
                default=u'Use the language of the content item'),
        description=_(u'description_language_of_the_content',
                      default=u'Use the language of the content item.'),
        default=False,
        required=False,
    )

    use_path_negotiation = schema.Bool(
        title=_(
            u'heading_language_codes_in_URL',
            default=u'Use language codes in URL path for manual override'),
        description=_(
            u'description_language_codes_in_URL',
            default=u'Use language codes in URL path for manual override.'),
        default=False,
        required=False,
    )

    use_cookie_negotiation = schema.Bool(
        title=_(u'heading_cookie_manual_override',
                default=(u'Use cookie for manual override')),
        description=_(
            u'description_cookie_manual_override',
            default=(
                u'Required for the language selector viewlet to be rendered.'
            )
        ),
        default=False,
        required=False,
    )

    authenticated_users_only = schema.Bool(
        title=_(u'heading_auth_cookie_manual_override',
                default=u'Authenticated users only'),
        description=_(
            u'description_auth_ookie_manual_override',
            default=(u'Related to: use cookie for manual override')
        ),
        default=False,
        required=False,
    )

    set_cookie_always = schema.Bool(
        title=_(
            u'heading_set_language_cookie_always',
            default=(u'Set the language cookie always')),
        description=_(
            u'description_set_language_cookie_always',
            default=(
                u'i.e. also when the \'set_language\' request parameter is '
                u'absent'
            )
        ),
        default=False,
        required=False,
    )

    use_subdomain_negotiation = schema.Bool(
        title=_(u'heading_use_subdomain',
                default=u'Use subdomain'),
        description=_(u'description_use_subdomain',
                      default=u'e.g.: de.plone.org'),
        default=False,
        required=False,
    )

    use_cctld_negotiation = schema.Bool(
        title=_(u'heading_top_level_domain',
                default=u'Use top-level domain'),
        description=_(u'description_top_level_domain',
                      default=u'e.g.: www.plone.de'),
        default=False,
        required=False,
    )

    use_request_negotiation = schema.Bool(
        title=_(u'heading_browser_language_request_negotiation',
                default=u'Use browser language request negotiation'),
        description=_(u'description_browser_language_request_negotiation',
                      default=u'Use browser language request negotiation.'),
        default=False,
        required=False,
    )
