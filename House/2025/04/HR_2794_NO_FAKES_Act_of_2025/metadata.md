# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2794?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2794
- Title: NO FAKES Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2794
- Origin chamber: House
- Introduced date: 2025-04-09
- Update date: 2025-12-05T22:08:08Z
- Update date including text: 2025-12-05T22:08:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-09: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-04-09: Introduced in House

## Actions

- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2794",
    "number": "2794",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "S000168",
        "district": "27",
        "firstName": "Maria",
        "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
        "lastName": "Salazar",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "NO FAKES Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T22:08:08Z",
    "updateDateIncludingText": "2025-12-05T22:08:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": {
          "date": "2025-04-09T16:04:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "PA"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "TX"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "VT"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "NY"
    },
    {
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-29",
      "state": "FL"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "NV"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "VA"
    },
    {
      "bioguideId": "F000483",
      "district": "30",
      "firstName": "Laura",
      "fullName": "Rep. Friedman, Laura [D-CA-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Friedman",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "CA"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "OH"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "FL"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2794ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2794\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2025 Ms. Salazar (for herself, Ms. Dean of Pennsylvania , Mr. Moran , Ms. Balint , and Mr. Morelle ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo protect intellectual property rights in the voice and visual likeness of individuals, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Nurture Originals, Foster Art, and Keep Entertainment Safe Act of 2025 or the NO FAKES Act of 2025 .\n#### 2. Voice and visual likeness rights\n##### (a) Definitions\nIn this section:\n**(1) Digital fingerprint**\nThe term digital fingerprint means an electronic label or identifier created by a cryptographic hash function (or similar function), or any other digital process, tool, or technique selected by the provider of an online service, that is unique to a specific piece of material such that it is effectively certain that such piece of material will not be misidentified as a match for a different piece of material.\n**(2) Digital replica**\nThe term digital replica \u2014\n**(A)**\nmeans a newly created, computer-generated, highly realistic electronic representation that is readily identifiable as the voice or visual likeness of an individual that\u2014\n**(i)**\nis embodied in a sound recording, image, audiovisual work, including an audiovisual work that does not have any accompanying sounds, or transmission\u2014\n**(I)**\nin which the actual individual did not actually perform or appear; or\n**(II)**\nthat is a version of a sound recording, image, or audiovisual work in which the actual individual did perform or appear, in which the fundamental character of the performance or appearance has been materially altered; and\n**(B)**\ndoes not include the electronic reproduction, use of a sample of one sound recording or audiovisual work into another, remixing, mastering, or digital remastering of a sound recording or audiovisual work authorized by the copyright holder.\n**(3) Individual**\nThe term individual means a human being, living or dead.\n**(4) Interactive computer service**\nThe term interactive computer service means any information service, system, or access software provider that provides or enables computer access by multiple users to a computer server, including specifically\u2014\n**(A)**\na service or system that provides access to the internet; and\n**(B)**\nsuch systems operated, or services offered, by libraries or educational institutions.\n**(5) Online service**\nThe term online service \u2014\n**(A)**\nmeans\u2014\n**(i)**\nany website, online application, mobile application, or virtual reality environment that predominantly provides public access to user uploaded material;\n**(ii)**\nany digital music provider to which section 115 of title 17, United States Code, applies that provides public access to user uploaded material if that digital music provider is not covered under clause (i); and\n**(iii)**\nany online application, mobile application, virtual reality environment, application store, search engine (including any feature that provides web search results), advertising service or network, online shopping service or platform, electronic commerce provider, mapping service, cloud storage service, or website hosting service or any other interactive computer service that is not covered under clause (i) and that provides public access to user uploaded material, but only if the provider of that interactive computer service has registered a designated agent with the Copyright Office under subsection (d)(2); and\n**(B)**\ndoes not include any website, online application, mobile application, virtual reality environment, application store, search engine, or cloud storage service that predominantly provides public access to user uploaded products or services, the primary function of which is to distribute, import, transmit, or otherwise make available to the public a product or service described in subsection (c)(2)(B).\n**(6) Right holder**\nThe term right holder means\u2014\n**(A)**\nthe individual, the voice or visual likeness of whom is at issue with respect to a digital replica or a product or service described in subsection (c)(2)(B); and\n**(B)**\nany other individual or entity that has acquired, through a license, inheritance, or otherwise, the right to authorize the use of the voice or visual likeness described in subparagraph (A).\n**(7) Sound recording artist**\nThe term sound recording artist means an individual who creates or performs in sound recordings for economic gain or for the livelihood of the individual.\n**(8) User uploaded material**\n**(A) In general**\nThe term user uploaded material means material, such as a video, image, game, audio file, or other material, that is placed on a service directly by or at the direction of an end user of a service.\n**(B) Scope of end user**\nFor the purposes of subparagraph (A), an end user, with respect to an online service, does not include\u2014\n**(i)**\na third-party commercial provider of sound recordings to a digital music provider; or\n**(ii)**\nan employee or agent of the online service acting on behalf of the provider of the online service.\n##### (b) Digital replication right\n**(1) In general**\nSubject to the other provisions of this section, each individual or right holder shall have the right to authorize the use of the voice or visual likeness of the individual\u2014\n**(A)**\nin a digital replica; or\n**(B)**\nin connection with a product or service for which authorization of the individual or right holder is required to avoid liability with respect to an activity described in subsection (c)(2)(B).\n**(2) Nature of right**\n**(A) In general**\nThe right described in paragraph (1) shall have the following characteristics:\n**(i)**\nThe right is\u2014\n**(I)**\na property right;\n**(II)**\nnot assignable during the life of the individual; and\n**(III)**\nlicensable, in whole or in part, exclusively or non-exclusively, by the right holder.\n**(ii)**\nThe right shall not expire upon the death of the individual, without regard to whether the right is commercially exploited by the individual during the lifetime of the individual.\n**(iii)**\nUpon the death of the individual\u2014\n**(I)**\nthe right is transferable and licensable, in whole or in part, by the executors, heirs, assigns, licensees, or devisees of the individual; and\n**(II)**\nownership of the right may be\u2014\n**(aa)**\ntransferred, in whole or in part, by any means of conveyance or by operation of law; and\n**(bb)**\nbequeathed by will or pass as personal property by the applicable laws of intestate succession.\n**(iv)**\nThe right shall be exclusive to\u2014\n**(I)**\nthe individual, subject to the licensing of the right during the lifetime of that individual under subparagraph (B); and\n**(II)**\nthe right holder\u2014\n**(aa)**\nfor a period of 10 years after the death of the individual; and\n**(bb)**\nif the right holder demonstrates active and authorized public use of the voice or visual likeness of the individual during the 2-year period preceding the expiration of the 10-year period described in item (aa), for an additional 5-year period, subject to renewal for additional 5-year periods, provided the right holder can demonstrate authorized public use of the voice or visual likeness of the individual during the 2-year period preceding the expiration of each additional 5-year period.\n**(v)**\nThe right shall terminate on the date that is the earlier of\u2014\n**(I)**\nthe date on which the 10-year period or 5-year period described in clause (iv)(II) terminates without renewal; or\n**(II)**\nthe date that is 70 years after the death of the individual.\n**(B) Requirements for license**\n**(i) In general**\nA license described in subparagraph (A)(i)(III)\u2014\n**(I)**\nwhile the individual is living, is valid only to the extent that the license duration does not exceed 10 years; and\n**(II)**\nshall be valid only if the license agreement\u2014\n**(aa)**\nis in writing and signed by the individual or an authorized representative of the individual; and\n**(bb)**\nincludes a reasonably specific description of the intended uses of the applicable digital replica.\n**(ii) Licenses involving a minor**\nA license described in subparagraph (A)(i)(III) involving a living individual who is younger than 18 years of age\u2014\n**(I)**\nis valid only to the extent that the license duration does not exceed 5 years, but in any case terminates when the individual reaches 18 years of age; and\n**(II)**\nshall be valid only if the license agreement\u2014\n**(aa)**\nis in writing and signed by the individual or an authorized representative of the individual;\n**(bb)**\nincludes a reasonably specific description of the intended uses of the digital replica; and\n**(cc)**\nis approved by a court in accordance with applicable State law.\n**(iii) Collective bargaining agreements**\nThe provisions of clauses (i) and (ii) shall not apply with respect to a license if the license is governed by a collective bargaining agreement that addresses digital replicas.\n**(iv) Limitation**\nThe provisions of clauses (i) and (ii) shall not affect terms and conditions of a license or related contract other than those described in this subparagraph, and the expiration of that license shall not affect the remainder of the license or related contract.\n**(C) Requirements for post-mortem transfer**\nA post-mortem transfer or license described in subparagraph (A)(iii)(I) shall be valid only if the transfer agreement or license agreement is in writing and signed by the right holder or an authorized representative of the right holder.\n**(D) Registration for post-mortem renewal**\n**(i) In general**\nThe renewal of a post-mortem right under subparagraph (A)(iv)(II)(bb) shall be effective if, during the applicable 2-year renewal period described in that subparagraph, the right holder files a notice with the Register of Copyrights that complies with such requirements regarding form and filing procedures as the Register of Copyrights may prescribe by regulation, which shall include\u2014\n**(I)**\nthe name of the deceased individual;\n**(II)**\na statement, under penalty of perjury, that the right holder has engaged in active and authorized public use of the voice or visual likeness during the applicable 2-year period;\n**(III)**\nthe identity of and contact information for the right holder; and\n**(IV)**\nsuch other information as the Register of Copyrights may prescribe by regulation.\n**(ii) Directory**\nThe Register of Copyrights\u2014\n**(I)**\nshall\u2014\n**(aa)**\nmaintain a current directory of post-mortem digital replication rights registered under this subparagraph; and\n**(bb)**\nmake the directory described in item (aa) available to the public for inspection online; and\n**(II)**\nmay require payment of a reasonable filing fee by the right holder filing notice under clause (i), which may take into consideration the costs of maintaining the directory described in subclause (I) of this clause.\n**(iii) Voluntary initial registration**\n**(I) In general**\nA right holder may voluntarily register the post-mortem right under subparagraph (A)(iv)(II)(aa) by filing a notice with the Register of Copyrights that complies with such requirements regarding form, content, and filing procedures as the Register of Copyrights may prescribe by regulation.\n**(II) Authority of Register of Copyrights**\nThe Register of Copyrights may\u2014\n**(aa)**\ninclude a voluntary registration of the post-mortem right under subparagraph (A)(iv)(II)(aa) in the directory maintained under clause (ii)(I)(aa) of this subparagraph; and\n**(bb)**\nrequire payment of a reasonable filing fee by a right holder registering a right under this clause, which may take into consideration the costs of maintaining the directory.\n**(iv) Authority of Register of Copyrights**\nThe Register of Copyrights may make such interpretations and resolve such ambiguities as may be appropriate to carry out this subparagraph.\n**(E) Post-expiration or termination utilization of authorized uses**\nA digital replica that is embodied in a sound recording, image, audiovisual work, including an audiovisual work that does not have any accompanying sounds, or transmission, and the use of which is authorized pursuant to the terms of a license, may continue to be utilized in a manner consistent with the terms of that license after the expiration or termination of the license.\n##### (c) Liability\n**(1) In general**\nAny individual or entity that, in a manner affecting interstate commerce (or using any means or facility of interstate commerce), engages in an activity described in paragraph (2) shall be liable in a civil action brought under subsection (e).\n**(2) Activities described**\nAn activity described in this paragraph is either of the following:\n**(A)**\nThe public display, distribution, transmission, or communication of, or the act of otherwise making available to the public, a digital replica without authorization by the applicable right holder.\n**(B)**\nDistributing, importing, transmitting, or otherwise making available to the public a product or service that\u2014\n**(i)**\nis primarily designed to produce 1 or more digital replicas of a specifically identified individual or individuals without the authorization of\u2014\n**(I)**\nsuch individual or individuals;\n**(II)**\nthe applicable right holder; or\n**(III)**\nthe law;\n**(ii)**\nhas only limited commercially significant purpose or use other than to produce a digital replica of a specifically identified individual or individuals without the authorization of\u2014\n**(I)**\nsuch individual or individuals;\n**(II)**\nthe applicable right holder; or\n**(III)**\nthe law; or\n**(iii)**\nis marketed, advertised, or otherwise promoted by the individual or entity described in paragraph (1), or another individual or entity acting in concert with the individual or entity described in paragraph (1) with the knowledge of the individual described in paragraph (1), as a product or service designed to produce a digital replica of a specifically identified individual or individuals without the authorization of\u2014\n**(I)**\nsuch individual or individuals;\n**(II)**\nthe applicable right holder; or\n**(III)**\nthe law.\n**(3) Notice or knowledge required**\nTo incur liability under this subsection\u2014\n**(A)**\nwith respect to an activity carried out under paragraph (2) by the provider of an online service, the provider must have received a notification that satisfies the requirements under subsection (d)(3), or a court order stating (or must have willfully avoided receipt of such a notification or court order), that the applicable material is\u2014\n**(i)**\na digital replica that was not authorized by the applicable right holder; or\n**(ii)**\na product or service described in paragraph (2)(B); and\n**(B)**\nwith respect to an activity carried out under paragraph (2) by an individual or entity that is not a provider of an online service, the individual or entity must have actual knowledge, or must willfully avoid having such knowledge, that the applicable material is\u2014\n**(i)**\na digital replica that was not authorized by the applicable right holder; or\n**(ii)**\na product or service described in paragraph (2)(B).\n**(4) Exclusions**\nLiability under this subsection shall not extend to\u2014\n**(A)**\na service by wire or radio that provides the capability to transmit data to and receive data from all, or substantially all, internet endpoints, including any capabilities that are incidental to enable the operation of the communications service of a provider of online services or network access, or the operator of facilities for such service; or\n**(B)**\na provider of an online service alleged to have undertaken an activity described in paragraph (2) if\u2014\n**(i)**\nit is not technologically feasible for that provider to disable access to the offending material, or disable the reference or link to that material, at the specific location identified in the applicable notification sent under subsection (d)(3); or\n**(ii)**\ndisabling access to the offending material is prohibited by law.\n**(5) Additional exclusions**\n**(A) In general**\nAn activity shall not be considered to be an activity described in paragraph (2) if\u2014\n**(i)**\nthe applicable digital replica is produced or used in a bona fide news, public affairs, or sports broadcast or account, provided that the digital replica is the subject of, or is materially relevant to, the subject of that broadcast or account;\n**(ii)**\nthe applicable digital replica is a representation of the applicable individual as the individual in a documentary or in a historical or biographical manner, including some degree of fictionalization, unless\u2014\n**(I)**\nthe production or use of that digital replica creates the false impression that the work is an authentic sound recording, image, transmission, or audiovisual work in which the individual participated; or\n**(II)**\nthe digital replica is embodied in a musical sound recording that is synchronized to accompany a motion picture or other audiovisual work, except to the extent that the use of that digital replica is protected by the First Amendment to the Constitution of the United States;\n**(iii)**\nthe applicable digital replica is produced or used consistent with the public interest in bona fide commentary, criticism, scholarship, satire, or parody;\n**(iv)**\nthe use of the applicable digital replica is fleeting or negligible; or\n**(v)**\nthe applicable digital replica is used in an advertisement or commercial announcement for a purpose described in any of clauses (i) through (iv) and the applicable digital replica is relevant to the subject of the work so advertised or announced.\n**(B) Applicability**\nSubparagraph (A) shall not apply where the applicable digital replica is used to depict sexually explicit conduct, as defined in section 2256(2)(A) of title 18, United States Code.\n##### (d) Safe harbors\n**(1) In general**\n**(A) Products and services capable of producing digital replicas**\nNo individual or entity shall be directly or secondarily liable under this section for an activity described in subsection (c)(2)(A) by virtue of distributing, importing, transmitting, or otherwise making available to the public a product or service unless the product or service is a product or service described in subsection (c)(2)(B).\n**(B) Online services**\nThe provider of an online service shall not be liable for referring or linking to, or violating subsection (c) with respect to, user uploaded material if\u2014\n**(i)**\nfor the provider of an online service described in subsection (a)(5)(A)(iii) (other than a search engine or a search component of a service), the provider has adopted and reasonably implemented, and has informed users of the online service of, a policy that provides for the termination in appropriate circumstances of account holders of the online service that are repeat violators of subsection (c)(2), provided that the failure to terminate a particular account holder in accordance with that policy shall subject the provider of the online service to potential liability only with respect to violating content posted by that account holder; and\n**(ii)**\nupon receiving a notification that satisfies the requirements under paragraph (3), the provider\u2014\n**(I)**\nremoves or disables access to the work embodying the claimed unauthorized digital replica or the product or service specifically identified in a notice sent under that paragraph, or, as applicable, the link or reference to the unauthorized digital replica or product or service, as soon as is technically and practically feasible for that provider;\n**(II)**\nfor the provider of an online service described in clause (i) or (ii) of subsection (a)(5)(A), as soon as is technically and practically feasible for that provider, removes or disables access to all other publicly available instances of the work embodying the claimed unauthorized digital replica that\u2014\n**(aa)**\nmatch the digital fingerprint of an unauthorized digital replica specifically identified in a notification sent under paragraph (3); and\n**(bb)**\nare uploaded after valid, applicable notice was submitted to, and processed by, the provider; and\n**(III)**\ntakes reasonable steps to promptly notify the right holder, and the end user that uploaded the material, that the online service removed or disabled access to the material.\n**(2) Designated agent**\n**(A) Designation**\n**(i) In general**\nA provider of an online service described in clause (i) or (ii) of subsection (a)(5)(A) shall register a designated agent in accordance with this paragraph.\n**(ii) Contents**\nTo designate an agent under clause (i), the provider of an online service shall make available through the online service, including on the website of the online service in a location accessible to the public, and provide to the Copyright Office, substantially the following information:\n**(I)**\nThe name, address, telephone number, and electronic mail address of the agent.\n**(II)**\nOther contact information that the Register of Copyrights may determine appropriate.\n**(B) Directory**\nThe Register of Copyrights\u2014\n**(i)**\nshall\u2014\n**(I)**\nmaintain a current directory of designated agents for the purposes of this paragraph; and\n**(II)**\nmake the directory described in subclause (I) available to the public for inspection, including through the internet; and\n**(ii)**\nmay require payment of a fee by the provider of an online service to cover the costs of maintaining the directory described in clause (i)(I).\n**(C) Effect of failure to designate**\nThe failure of a provider of an online service described in subparagraph (A)(i) to register a designated agent under this paragraph shall establish that the provider has not undertaken a good faith effort to comply with this subsection.\n**(3) Elements of notification**\nTo be effective under this subsection, a notification of a claimed violation of the right described in subsection (b) shall be a written communication provided to the designated agent of the provider of an online service that includes the following:\n**(A)**\nA physical or electronic signature of the right holder, an individual or entity authorized to act on behalf of the right holder, or an eligible plaintiff under subsection (e)(1).\n**(B)**\nIdentification of the individual, the voice or visual likeness of whom is at issue with respect to an unauthorized digital replica or a product or service described in subsection (c)(2)(B).\n**(C)**\nIdentification of the material containing an unauthorized digital replica or a product or service described in subsection (c)(2)(B), including information sufficient to allow the provider to locate the identified material.\n**(D)**\nInformation reasonably sufficient to permit the provider to contact the notifying party, such as an address, telephone number, and email address.\n**(E)**\nA statement that the notifying party believes in good faith that the material is an unauthorized use of a digital replica or a product or service described in subsection (c)(2)(B).\n**(F)**\nIf not the right holder or an eligible plaintiff under subsection (e)(1), a statement that the notifying party has the authority to act on behalf of the right holder.\n**(G)**\nFor the purposes of paragraph (1)(B), information reasonably sufficient to\u2014\n**(i)**\nidentify the reference or link to the material or activity claimed to be an unauthorized digital replica, or a product or service described in subsection (c)(2)(B), that is to be removed or to which access is to be disabled; and\n**(ii)**\npermit the provider to locate the reference or link described in clause (i).\n**(4) Penalties for false or deceptive notice**\n**(A) Knowing material representations**\n**(i) In general**\nIt shall be unlawful to knowingly materially misrepresent under paragraph (3)\u2014\n**(I)**\nthat the material requested to be removed is an unauthorized digital replica;\n**(II)**\nthat an individual or entity has the authority to act on behalf of the right holder; or\n**(III)**\nthat a digital replica or a product or service described in subsection (c)(2)(B) is not authorized by the right holder or by other law.\n**(ii) Failure to perform good faith review**\nThe failure to undertake a good faith review to determine whether material with respect to which notice is provided under paragraph (3) qualifies as a digital replica shall constitute a knowing material misrepresentation under this subparagraph.\n**(B) Penalties**\nIn addition to a cause of action that is available under subsection (e), any individual or entity that violates subparagraph (A) of this paragraph shall be liable to the alleged violator that uploaded the applicable material, or the provider of an online service injured by the misrepresentation, for an amount equal to the greater of\u2014\n**(i)**\n$25,000 per notification sent under paragraph (3) that contains a misrepresentation described in subparagraph (A) of this paragraph; or\n**(ii)**\nany actual damages, including costs and attorney\u2019s fees, incurred by the alleged violator, as well as by any provider of an online service injured by the reliance of the provider on the misrepresentation in removing or disabling access to the material or activity claimed to be an unauthorized digital replica.\n##### (e) Civil action\n**(1) Eligible plaintiffs**\nA civil action against an individual or entity that, in a manner affecting interstate commerce (or using any means or facility of interstate commerce), engages in an activity described in subsection (c)(2) may be brought by\u2014\n**(A)**\nthe applicable right holder;\n**(B)**\nif the applicable right holder is an individual who is younger than 18 years of age, a parent or guardian of that individual; or\n**(C)**\nin the case of a digital replica involving a sound recording artist, any individual or entity that has, directly or indirectly, entered into\u2014\n**(i)**\na contract for the exclusive personal services of the sound recording artist as a sound recording artist; or\n**(ii)**\nan exclusive license to distribute or transmit 1 or more works that capture the audio performance of the sound recording artist.\n**(2) Limitations period**\nA civil action may not be brought under this subsection unless the civil action is commenced not later than 3 years after the date on which the party seeking to bring the civil action discovered, or with due diligence should have discovered, the applicable violation.\n**(3) Defense not permitted**\nIt shall not be a defense in a civil action brought under this subsection that the defendant displayed or otherwise communicated to the public a disclaimer stating that the applicable digital replica, or the applicable product or service described in subsection (c)(2)(B), was unauthorized or disclosed that the digital replica, product, or service was generated through the use of artificial intelligence or other technology.\n**(4) Remedies**\n**(A) In general**\nIn any civil action brought under this subsection\u2014\n**(i)**\nan individual or entity that engages in an activity described in subsection (c)(2)(A) shall be liable to the injured party in an amount equal to the greater of\u2014\n**(I)**\n**(aa)**\nin the case of an individual, $5,000 per work embodying the applicable unauthorized digital replica;\n**(bb)**\nin the case of a provider of an online service that has undertaken a good faith effort to comply with subsection (d), $25,000 per work embodying the applicable unauthorized digital replica;\n**(cc)**\nin the case of a provider of an online service that has not undertaken a good faith effort to comply with subsection (d), $5,000 per display, copy made, transmission, and instance of the unauthorized digital replica being made available on the online service in a sum of not more than $750,000 per work embodying the applicable unauthorized digital replica; and\n**(dd)**\nin the case of an entity that is not a provider of an online service, $25,000 per work embodying the applicable unauthorized digital replica; or\n**(II)**\nany actual damages suffered by the injured party as a result of the activity, plus any profits from the unauthorized use that are attributable to such use and are not taken into account in computing the actual damages;\n**(ii)**\nan individual or entity that engages in an activity described in subsection (c)(2)(B) shall be liable to the injured party in an amount equal to the greater of\u2014\n**(I)**\n**(aa)**\nin the case of an individual, $5,000 per product or service;\n**(bb)**\nin the case of a provider of an online service that has undertaken a good faith effort to comply with subsection (d), $25,000 per product or service;\n**(cc)**\nin the case of a provider of an online service that has not undertaken a good faith effort to comply with subsection (d), $750,000 per product or service; or\n**(dd)**\nin the case of an entity that is not a provider of an online service, $25,000 per product or service; or\n**(II)**\nany actual damages suffered by the injured party as a result of the activity, plus any profits from the unauthorized use that are attributable to such use and are not taken into account in computing the actual damages;\n**(iii)**\nthe plaintiff may seek injunctive or other equitable relief;\n**(iv)**\nin the case of willful activity in which the injured party has proven that the defendant acted with malice, fraud, knowledge, or willful avoidance of knowledge that the conduct violated the law, the court may award to the injured party punitive damages; and\n**(v)**\nif the prevailing party is\u2014\n**(I)**\nthe party bringing the action, the court shall award reasonable attorney\u2019s fees; or\n**(II)**\nthe party defending the action, the court shall award reasonable attorney\u2019s fees if the court determines that the action was not brought in good faith.\n**(B) Objectively reasonable belief**\nA provider of an online service that has designated an agent under subsection (d)(2) and has an objectively reasonable belief that material that is claimed to be an unauthorized digital replica does not qualify as a digital replica shall be liable only for actual damages under subparagraph (A) if the material is ultimately determined to be an unauthorized digital replica.\n**(C) Replacement of removed material**\nIf the end user that uploaded the material that the provider of an online service has removed, or to which the provider of an online service has disabled access, brings an action in a court of the United States against the sender of a notification under subsection (d)(3) claiming that such notification was false or deceptive, as described in subsection (d)(4), the provider may, if the action is brought not later than 14 days after the end user receives notice that the provider has removed or disabled access to the material, restore the removed material to the network of the provider for access by members of the public without monetary liability therefor to either the notice sender or the end user that uploaded the material to which the provider had removed or disabled access.\n##### (f) Subpoena To identify violator\n**(1) Request**\nA right holder, an individual or entity authorized to act on behalf of a right holder, or an eligible plaintiff under subsection (e)(1) may request the clerk of any district court of the United States to issue a subpoena to a provider of an online service for identification of an alleged violator of this section in accordance with this subsection.\n**(2) Contents of request**\nA request under paragraph (1) may be made by filing with the clerk\u2014\n**(A)**\na copy of a notification described in subsection (d)(3);\n**(B)**\na proposed subpoena; and\n**(C)**\na sworn declaration to the effect that\u2014\n**(i)**\nthe purpose of the subpoena is to obtain the identity of an individual or entity alleged to be liable under subsection (c); and\n**(ii)**\nthe information described in clause (i) will only be used for the purpose of protecting rights under this section.\n**(3) Contents of subpoena**\nA subpoena issued under this subsection shall authorize and order the provider of the applicable online service to expeditiously disclose to the party that sought the subpoena information sufficient to identify the alleged violator by virtue of the activity described in the notification to the extent that information is available to the provider of the online service.\n**(4) Basis for granting subpoena**\nIf a proposed subpoena under this subsection is in proper form, the applicable notification filed satisfies the requirements under subsection (d)(3), and the accompanying declaration is properly executed, the clerk shall expeditiously issue and sign the proposed subpoena and return the subpoena to the requester for delivery to the provider of the applicable online service.\n##### (g) Preemption\n**(1) In general**\nThe rights established under this Act shall preempt any cause of action under State law for the protection of an individual\u2019s voice and visual likeness rights in connection with a digital replica, as defined in this Act, in an expressive work.\n**(2) Rule of construction**\nNotwithstanding paragraph (1), nothing in this Act may be construed to preempt\u2014\n**(A)**\ncauses of action under State statutes or common law in existence, as of January 2, 2025, regarding a digital replica;\n**(B)**\ncauses of action under State statutes specifically regulating a digital replica depicting sexually explicit conduct, as defined in section 2256(2)(A) of title 18, United States Code, or an election-related digital replica; or\n**(C)**\ncauses of action under State statutes or common law in existence, as of January 2, 2025, for the distributing, importing, transmitting, or otherwise making available to the public a product or service capable of producing 1 or more digital replicas.\n##### (h) Rules of construction\n**(1) Laws pertaining to intellectual property**\nThis section shall be considered to be a law pertaining to intellectual property for the purposes of section 230(e)(2) of the Communications Act of 1934 ( 47 U.S.C. 230(e)(2) ).\n**(2) No duty to monitor**\nExcept as expressly provided in subsection (d)(1)(B)(ii), nothing in this section may be construed to require the provider of an online service to\u2014\n**(A)**\nmonitor the online service for, or affirmatively seek facts about, any digital replica; or\n**(B)**\ngain access to material.\n##### (i) Severability\nIf any provision of this section, or the application of a provision of this section, is held to be invalid, the validity of the remainder of this section, and the application of that provision to other individuals, entities, and circumstances, shall not be affected by that holding.\n##### (j) Retroactive effect\n**(1) Liabilities**\nLiability under this section shall apply only to\u2014\n**(A)**\nconduct occurring after the date of enactment of this Act; and\n**(B)**\nin the case of conduct covered by a license or contract, a license or contract that is executed after the date of enactment of this Act.\n**(2) Digital replication right**\nThe right granted under subsection (b)\u2014\n**(A)**\nshall apply to any individual, regardless of whether the individual dies before or after the date of enactment of this Act; and\n**(B)**\nin the case of a right holder who has died before the date of enactment of this Act, shall vest in the executors, heirs, assigns, or devisees of the right holder.\n##### (k) Effective date\nThis Act shall take effect on the date that is 180 days after the date of enactment of this Act.",
      "versionDate": "2025-04-09",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-09",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "1367",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "NO FAKES Act of 2025",
      "type": "S"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-09-03T20:28:24Z"
          },
          {
            "name": "Administrative remedies",
            "updateDate": "2025-09-03T20:28:24Z"
          },
          {
            "name": "Art, artists, authorship",
            "updateDate": "2025-09-03T20:28:24Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-09-03T20:28:24Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-09-03T20:28:24Z"
          },
          {
            "name": "Department of Commerce",
            "updateDate": "2025-09-03T20:28:24Z"
          },
          {
            "name": "Digital media",
            "updateDate": "2025-09-03T20:28:24Z"
          },
          {
            "name": "Federal preemption",
            "updateDate": "2025-09-03T20:28:24Z"
          },
          {
            "name": "Intellectual property",
            "updateDate": "2025-09-03T20:28:24Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-09-03T20:28:24Z"
          },
          {
            "name": "Music",
            "updateDate": "2025-09-03T20:28:24Z"
          },
          {
            "name": "Photography and imaging",
            "updateDate": "2025-09-03T20:28:24Z"
          },
          {
            "name": "Sound recording",
            "updateDate": "2025-09-03T20:28:24Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-05-19T15:27:21Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2794ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "NO FAKES Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-25T08:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "NO FAKES Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-25T08:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Nurture Originals, Foster Art, and Keep Entertainment Safe Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-25T08:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To protect intellectual property rights in the voice and visual likeness of individuals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-25T08:18:35Z"
    }
  ]
}
```
