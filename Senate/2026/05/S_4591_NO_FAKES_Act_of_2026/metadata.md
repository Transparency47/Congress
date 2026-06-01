# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4591?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4591
- Title: NO FAKES Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4591
- Origin chamber: Senate
- Introduced date: 2026-05-20
- Update date: 2026-05-30T04:53:26Z
- Update date including text: 2026-05-30T04:53:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-20: Introduced in Senate
- 2026-05-20 - IntroReferral: Introduced in Senate
- 2026-05-20 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-05-20: Introduced in Senate

## Actions

- 2026-05-20 - IntroReferral: Introduced in Senate
- 2026-05-20 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-20",
    "latestAction": {
      "actionDate": "2026-05-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4591",
    "number": "4591",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "C001088",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Coons, Christopher A. [D-DE]",
        "lastName": "Coons",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "NO FAKES Act of 2026",
    "type": "S",
    "updateDate": "2026-05-30T04:53:26Z",
    "updateDateIncludingText": "2026-05-30T04:53:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-05-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2026-05-20T17:57:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "TN"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "MN"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "NC"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "IL"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "AL"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "HI"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "FL"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "VT"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "LA"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "CA"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "TN"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "MI"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4591is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4591\nIN THE SENATE OF THE UNITED STATES\nMay 20, 2026 Mr. Coons (for himself, Mrs. Blackburn , Ms. Klobuchar , Mr. Tillis , Mr. Durbin , Mrs. Britt , Ms. Hirono , Mrs. Moody , Mr. Welch , Mr. Cassidy , Mr. Schiff , Mr. Hagerty , Ms. Slotkin , and Mr. Lankford ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo protect intellectual property rights in the voice and visual likeness of individuals, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Nurture Originals, Foster Art, and Keep Entertainment Safe Act of 2026 or the NO FAKES Act of 2026 .\n#### 2. Voice and visual likeness rights\n##### (a) Definitions\nIn this section:\n**(1) Digital fingerprint**\nThe term digital fingerprint means an electronic label or identifier created by a cryptographic hash function (or similar function), or any other digital process, tool, or technique selected by the provider of an online service, that is unique to a specific piece of material such that it is effectively certain that such piece of material will not be misidentified as a match for a different piece of material.\n**(2) Digital replica**\nThe term digital replica \u2014\n**(A)**\nmeans a newly created, computer-generated, highly realistic electronic representation that is readily identifiable as the voice or visual likeness of an individual that\u2014\n**(i)**\nis embodied in a sound recording, image, audiovisual work, including an audiovisual work that does not have any accompanying sounds, or transmission\u2014\n**(I)**\nin which the actual individual did not actually perform or appear; or\n**(II)**\nthat is a version of a sound recording, image, or audiovisual work in which the actual individual did perform or appear, in which the fundamental character of the performance or appearance has been materially altered; and\n**(B)**\ndoes not include the electronic reproduction, use of a sample of one sound recording or audiovisual work into another, remixing, mastering, or digital remastering of a sound recording or audiovisual work authorized by the copyright holder.\n**(3) Individual**\nThe term individual means a human being, living or dead.\n**(4) Interactive computer service**\nThe term interactive computer service means any information service, system, or access software provider that provides or enables computer access by multiple users to a computer server, including specifically\u2014\n**(A)**\na service or system that provides access to the internet; and\n**(B)**\nsuch systems operated, or services offered, by libraries or educational institutions.\n**(5) Online service**\nThe term online service \u2014\n**(A)**\nmeans\u2014\n**(i)**\nany website, online application, mobile application, or virtual reality environment that predominantly provides public access to user uploaded material;\n**(ii)**\nany digital music provider to which section 115 of title 17, United States Code, applies, to the extent that the digital music provider provides public access to a significant amount of sound recordings that are predominantly the fixation of sounds of a performance of a musical composition and are user uploaded material, if that digital music provider is not covered under clause (i); and\n**(iii)**\nany online application, mobile application, virtual reality environment, application store, search engine (including any feature that provides web search results), advertising service or network, online shopping service or platform, electronic commerce provider, mapping service, cloud storage service, aggregator of visual and audiovisual works for licensing, or website hosting service or any other interactive computer service that is not covered under clause (i), and is not a digital music provider to which section 115 of title 17, United States Code, applies, but only if the provider of that interactive computer service has registered a designated agent with the Copyright Office under subsection (d)(2); and\n**(B)**\ndoes not include any website, online application, mobile application, virtual reality environment, application store, cloud storage service, or search engine, if the primary function of that website, online application, mobile application, virtual reality environment, application store, cloud storage service, or search engine is to distribute, import, transmit, or otherwise make available to the public a product or service described in subsection (c)(2)(B).\n**(6) Right holder**\nThe term right holder means\u2014\n**(A)**\nthe individual, the voice or visual likeness of whom is at issue with respect to a digital replica or a product or service described in subsection (c)(2)(B); and\n**(B)**\nany other individual or entity that has acquired, through a license, inheritance, or otherwise, the right to authorize the use of the voice or visual likeness described in subparagraph (A).\n**(7) Sound recording artist**\nThe term sound recording artist means an individual who creates or performs in sound recordings for economic gain or for the livelihood of the individual.\n**(8) User uploaded material**\nThe term user uploaded material means material, such as a video, image, game, audio file, or other similar material, that is placed on a service directly by, or at the direction of, a consumer end user of a service.\n##### (b) Digital replication right\n**(1) In general**\nSubject to the other provisions of this section, each individual or right holder shall have the right to authorize the use of the voice or visual likeness of the individual\u2014\n**(A)**\nin a digital replica; or\n**(B)**\nin connection with a product or service for which authorization of the individual or right holder is required to avoid liability with respect to an activity described in subsection (c)(2)(B).\n**(2) Nature of right**\n**(A) In general**\nThe right described in paragraph (1) shall have the following characteristics:\n**(i)**\nThe right is\u2014\n**(I)**\na property right;\n**(II)**\nnot assignable during the life of the individual; and\n**(III)**\nlicensable, in whole or in part, exclusively or non-exclusively, by the right holder.\n**(ii)**\nThe right shall not expire upon the death of the individual, without regard to whether the right is commercially exploited by the individual during the lifetime of the individual.\n**(iii)**\nUpon the death of the individual\u2014\n**(I)**\nthe right is transferable and licensable, in whole or in part, by the executors, heirs, assignees, licensees, or devisees of the individual; and\n**(II)**\nownership of the right may be\u2014\n**(aa)**\ntransferred, in whole or in part, by any means of conveyance or by operation of law; and\n**(bb)**\nbequeathed by will or pass as personal property by the applicable laws of intestate succession.\n**(iv)**\nThe right shall be exclusive to\u2014\n**(I)**\nthe individual, subject to the licensing of the right during the lifetime of that individual under subparagraph (B); and\n**(II)**\nthe right holder\u2014\n**(aa)**\nfor a period of 10 years after the death of the individual; and\n**(bb)**\nif the right holder demonstrates active and authorized public use of the voice or visual likeness of the individual in interstate or foreign commerce during the 2-year period preceding the expiration of the 10-year period described in item (aa), for an additional 5-year period, subject to renewal for additional 5-year periods, provided the right holder can demonstrate authorized public use of the voice or visual likeness of the individual in interstate or foreign commerce during the 2-year period preceding the expiration of each additional 5-year period.\n**(v)**\nThe right shall terminate on the date that is the earlier of\u2014\n**(I)**\nthe date on which the 10-year period or 5-year period described in clause (iv)(II) terminates without renewal; or\n**(II)**\nthe date that is 70 years after the death of the individual.\n**(B) Requirements for license**\n**(i) In general**\nA license described in subparagraph (A)(i)(III)\u2014\n**(I)**\nwhile the individual is living, is valid only to the extent that the license duration does not exceed 10 years; and\n**(II)**\nshall be valid only if the license agreement\u2014\n**(aa)**\nis in writing and signed by the individual or an authorized representative of the individual; and\n**(bb)**\nincludes a reasonably specific description of the intended uses of the applicable digital replica.\n**(ii) Licenses involving a minor**\nA license described in subparagraph (A)(i)(III) involving a living individual who is younger than 18 years of age\u2014\n**(I)**\nis valid only to the extent that the license duration does not exceed 5 years, but in any case terminates when the individual reaches 18 years of age; and\n**(II)**\nshall be valid only if the license agreement\u2014\n**(aa)**\nis in writing and signed by the individual or an authorized representative of the individual;\n**(bb)**\nincludes a reasonably specific description of the intended uses of the digital replica; and\n**(cc)**\nis approved by a court in accordance with applicable State law.\n**(iii) Collective bargaining agreements**\nThe provisions of clauses (i) and (ii) shall not apply with respect to a license if the license is governed by a collective bargaining agreement that addresses digital replicas.\n**(iv) Limitation**\nThe provisions of clauses (i) and (ii) shall not affect terms and conditions of a license or related contract other than those described in this subparagraph, and the expiration of that license shall not affect the remainder of the license or related contract.\n**(C) Requirements for post-mortem transfer**\nA post-mortem transfer or license described in subparagraph (A)(iii)(I) shall be valid only if the transfer agreement or license agreement is in writing and signed by the right holder or an authorized representative of the right holder.\n**(D) Registration for post-mortem renewal**\n**(i) In general**\nThe renewal of a post-mortem right under subparagraph (A)(iv)(II)(bb) shall be effective if, during the applicable 2-year renewal period described in that subparagraph, the right holder files a notice with the Register of Copyrights that complies with such requirements regarding form and filing procedures as the Register of Copyrights may prescribe by regulation, which shall include\u2014\n**(I)**\nthe name of the deceased individual;\n**(II)**\na statement, under penalty of perjury, that the right holder has engaged in active and authorized public use of the voice or visual likeness in interstate or foreign commerce during the applicable 2-year period;\n**(III)**\nthe identity of and contact information for the right holder; and\n**(IV)**\nsuch other information as the Register of Copyrights may prescribe by regulation.\n**(ii) Directory**\nThe Register of Copyrights\u2014\n**(I)**\nshall\u2014\n**(aa)**\nmaintain a current directory of post-mortem digital replication rights registered under this subparagraph; and\n**(bb)**\nmake the directory described in item (aa) available to the public for inspection online; and\n**(II)**\nmay require payment of a reasonable filing fee by the right holder filing notice under clause (i), which may take into consideration the costs of maintaining the directory described in subclause (I) of this clause.\n**(iii) Voluntary initial registration**\n**(I) In general**\nA right holder may voluntarily register the post-mortem right under subparagraph (A)(iv)(II)(aa) by filing a notice with the Register of Copyrights that complies with such requirements regarding form, content, and filing procedures as the Register of Copyrights may prescribe by regulation.\n**(II) Authority of Register of Copyrights**\nThe Register of Copyrights may\u2014\n**(aa)**\ninclude a voluntary registration of the post-mortem right under subparagraph (A)(iv)(II)(aa) in the directory maintained under clause (ii)(I)(aa) of this subparagraph; and\n**(bb)**\nrequire payment of a reasonable filing fee by a right holder registering a right under this clause, which may take into consideration the costs of maintaining the directory.\n**(iv) Authority of Register of Copyrights**\nThe Register of Copyrights may make such interpretations and resolve such ambiguities as may be appropriate to carry out this subparagraph.\n**(E) Post-expiration or termination utilization of authorized uses**\nA digital replica that is embodied in a sound recording, image, audiovisual work, including an audiovisual work that does not have any accompanying sounds, or transmission, and the use of which is authorized pursuant to the terms of a license, may continue to be utilized in a manner consistent with the terms of that license after the expiration or termination of the license.\n##### (c) Liability\n**(1) In general**\nAny individual or entity that, in a manner affecting interstate or foreign commerce (or using any means or facility of interstate or foreign commerce), engages in an activity described in paragraph (2) shall be liable in a civil action brought under subsection (e).\n**(2) Activities described**\nAn activity described in this paragraph is either of the following:\n**(A)**\nThe public display, distribution, transmission, or communication of, or the act of otherwise making available to the public, including by acting as a third party commercial supplier of sound recordings to a digital music provider, a digital replica without authorization by the applicable right holder.\n**(B)**\nDistributing, importing, transmitting, or otherwise making available to the public a product or service that\u2014\n**(i)**\nis primarily designed to produce 1 or more digital replicas of a specifically identified individual or individuals without the authorization of\u2014\n**(I)**\nsuch individual or individuals;\n**(II)**\nthe applicable right holder; or\n**(III)**\nthe law;\n**(ii)**\nhas only limited commercially significant purpose or use other than to produce a digital replica of a specifically identified individual or individuals without the authorization of\u2014\n**(I)**\nsuch individual or individuals;\n**(II)**\nthe applicable right holder; or\n**(III)**\nthe law; or\n**(iii)**\nis marketed, advertised, or otherwise promoted by the individual or entity described in paragraph (1), or another individual or entity acting in concert with the individual or entity described in paragraph (1) with the knowledge of the individual or entity described in paragraph (1), as a product or service designed to produce a digital replica of a specifically identified individual or individuals without the authorization of\u2014\n**(I)**\nsuch individual or individuals;\n**(II)**\nthe applicable right holder; or\n**(III)**\nthe law.\n**(3) Notice or knowledge required**\nTo incur liability under this subsection, the following shall apply:\n**(A)**\n**(i)**\nWith respect to an activity carried out under paragraph (2) by the provider of an online service described in clause (ii), the designated agent with respect to the provider must have received a notification that satisfies the requirements under subsection (d)(3), or a court order stating, or must have willfully avoided receipt of such a notification or court order, that the applicable material is\u2014\n**(I)**\na digital replica that was not authorized by the applicable right holder; or\n**(II)**\na product or service described in paragraph (2)(B).\n**(ii)**\nAn online service described in this clause is an online service that is\u2014\n**(I)**\ndescribed in subsection (a)(5)(A)(i);\n**(II)**\ndescribed in subsection (a)(5)(A)(ii), with respect to sound recordings that are predominantly the fixation of sounds of a performance of a musical composition and are user uploaded material; or\n**(III)**\ndescribed in subsection (a)(5)(A)(iii), with respect to material placed on that online service by or at the direction of a third party.\n**(B)**\nWith respect to an activity carried out under paragraph (2) by an individual or entity that is not an online service, or an activity carried out under paragraph (2) by the provider of an online service that is not described in subparagraph (A)(ii), the individual or entity must have actual knowledge, or must willfully avoid having such knowledge, that the applicable material is\u2014\n**(i)**\na digital replica that was not authorized by the applicable right holder; or\n**(ii)**\na product or service described in paragraph (2)(B).\n**(4) Exclusions**\nLiability under this subsection shall not extend to\u2014\n**(A)**\na service by wire or radio that provides the capability to transmit data to and receive data from all, or substantially all, internet endpoints, including any capabilities that are incidental to enable the operation of the communications service of a provider of online services or network access, or the operator of facilities for such service;\n**(B)**\na provider of an online service described in paragraph (3)(A)(ii) alleged to have undertaken an activity described in paragraph (2) if\u2014\n**(i)**\nit is not technologically or practically feasible for that provider to disable access to the offending material, or disable the reference or link to that material, at the specific location identified in the applicable notification sent under subsection (d)(3); or\n**(ii)**\ndisabling access to the offending material is prohibited by law;\n**(C)**\na nonprofit library or archives\u2014\n**(i)**\nthat is eligible for the limitations on exclusive rights under section 108 of title 17, United States Code;\n**(ii)**\nthe collections of which are\u2014\n**(I)**\nopen to the public; or\n**(II)**\navailable not only to researchers affiliated with the library or archives, or with the institution of which the library or archives is a part, but also to other persons doing research in a specialized field;\n**(iii)**\nthat has a public service mission;\n**(iv)**\nthe trained staff or volunteers of which provide professional services normally associated with libraries and archives; and\n**(v)**\nthe collections of which are composed of lawfully acquired or licensed materials that are made available consistent with the requirements of title 17, United States Code;\n**(D)**\nan accredited nonprofit educational institution with respect to an activity undertaken without any purpose of direct or indirect commercial advantage;\n**(E)**\nan employee of an institution described in subparagraph (C) or (D) acting within the scope of the employment of that individual;\n**(F)**\nany other person solely with respect to providing online or network access services to an institution described in subparagraph (C) or (D) in the course of providing those services to that institution; or\n**(G)**\nan individual or entity that is not an online service, if, upon obtaining actual knowledge of an activity described in paragraph (2), the individual or entity acts as soon as technologically and practically feasible to remove or disable access to the applicable material.\n**(5) Additional exclusions**\n**(A) In general**\nAn activity shall not be considered to be an activity described in paragraph (2) if\u2014\n**(i)**\nthe applicable digital replica is produced or used in a bona fide news, public affairs, or sports broadcast or account, provided that the digital replica is the subject of, or is materially relevant to, the subject of that broadcast or account;\n**(ii)**\nthe applicable digital replica is a representation of the applicable individual as the individual in a documentary or in a historical or biographical manner, including some degree of fictionalization, unless\u2014\n**(I)**\nthe production or use of that digital replica creates the false impression that the work is an authentic sound recording, image, transmission, or audiovisual work in which the individual participated; or\n**(II)**\nthe digital replica is embodied in a musical sound recording that is synchronized to accompany a motion picture or other audiovisual work, except to the extent that the use of that digital replica is protected by the First Amendment to the Constitution of the United States;\n**(iii)**\nthe applicable digital replica is produced or used consistent with the public interest in bona fide commentary, criticism, scholarship, satire, or parody;\n**(iv)**\nthe use of the applicable digital replica is fleeting or negligible; or\n**(v)**\nthe applicable digital replica is used in an advertisement or commercial announcement for a purpose described in any of clauses (i) through (iv) and the applicable digital replica is relevant to the subject of the work so advertised or announced.\n**(B) Applicability**\nSubparagraph (A) shall not apply where the applicable digital replica is used to depict sexually explicit conduct, as defined in section 2256(2)(A) of title 18, United States Code.\n**(6) Voluntary use of tools to remove or disable access**\nThe voluntary use of any tool to remove or disable access to content shall not alone confer actual knowledge of a particular violation of this section.\n##### (d) Safe harbors\n**(1) In general**\n**(A) Products and services capable of producing digital replicas**\nNo individual or entity shall be directly or secondarily liable under this section for an activity described in subsection (c)(2)(A) by virtue of distributing, importing, transmitting, or otherwise making available to the public a product or service unless the product or service is a product or service described in subsection (c)(2)(B).\n**(B) Online services**\nThe provider of an online service shall not be liable for an activity that violates subsection (c), or for referring or linking to the material containing an unauthorized digital replica or a product or service described in subsection (c)(2)(B), if\u2014\n**(i)**\nfor the provider of an online service described in subsection (a)(5)(A)(iii) (other than a search engine or a search component of a service), the provider has adopted and reasonably implemented, and has informed users of the online service of, a policy that provides for the termination in appropriate circumstances of account holders of the online service that are repeat violators of subsection (c)(2), provided that the failure to terminate a particular account holder in accordance with that policy shall subject the provider of the online service to potential liability only with respect to violating content posted by that account holder; and\n**(ii)**\n**(I)**\nupon receiving a notification that satisfies the requirements under paragraph (3), the provider\u2014\n**(aa)**\nremoves or disables access to the work embodying the claimed unauthorized digital replica or the product or service specifically identified in a notice sent under that paragraph, or, as applicable, the link or reference to the unauthorized digital replica or product or service, as soon as is technologically and practically feasible for that provider;\n**(bb)**\nfor the provider of an online service described in subsection (a)(5)(A)(i), as soon as is technologically and practically feasible for that provider, removes or disables access to all other publicly available instances of the work embodying the claimed unauthorized digital replica that\u2014\n(AA)\nmatch the digital fingerprint of an unauthorized digital replica specifically identified in a notification sent under paragraph (3); and\n(BB)\nare uploaded after valid, applicable notice was submitted to, and processed by, the provider;\n**(cc)**\nfor the provider of an online service described in subsection (a)(5)(A)(ii), with respect to sound recordings that are predominantly the fixation of sounds of a performance of a musical composition and are user uploaded material, as soon as is technologically and practically feasible for that provider, removes or disables access to all other publicly available instances of the work embodying the claimed unauthorized digital replica that\u2014\n(AA)\nmatch the digital fingerprint of an unauthorized digital replica specifically identified in a notification sent under paragraph (3); and\n(BB)\nare uploaded after valid, applicable notice was submitted to, and processed by, the provider; and\n**(dd)**\ntakes reasonable steps to promptly notify the right holder, and the party that placed the material on the online service, that the online service removed or disabled access to the material; and\n**(II)**\nthe provider, in the case that the provider receives a counter-notification that satisfies the requirements under paragraph (4) and opts to replace the removed material or cease disabling access to that material\u2014\n**(aa)**\ntakes reasonable steps to promptly provide the individual or entity that provided the applicable notification under paragraph (3) with a copy of the counter-notification; and\n**(bb)**\nnot less than 14 days after the date on which the provider receives that counter-notification, replaces the removed material or ceases disabling access to that material, unless an eligible plaintiff described in subsection (e) brings an action under that subsection, in which case the provider shall remove the material or disable access to the material as soon as is technologically and practically feasible for the provider.\n**(2) Designated agent**\n**(A) Designation**\n**(i) In general**\nA provider of an online service described in clause (i) or (ii) of subsection (a)(5)(A) shall, and a provider of an online service that is described in subsection (a)(5)(A)(iii) and is eligible for registration may, register a designated agent in accordance with this paragraph.\n**(ii) Contents**\nTo designate an agent under clause (i), the provider of an online service shall make available through that online service, in a location accessible to the public, and provide to the Copyright Office, substantially the following information:\n**(I)**\nThe name, address, telephone number, and electronic mail address of the agent.\n**(II)**\nOther contact information that the Register of Copyrights may determine appropriate.\n**(B) Directory**\nThe Register of Copyrights\u2014\n**(i)**\nshall\u2014\n**(I)**\nmaintain a current directory of designated agents for the purposes of this paragraph; and\n**(II)**\nmake the directory described in subclause (I) available to the public for inspection, including through the internet; and\n**(ii)**\nmay require payment of a fee by the provider of an online service to cover the costs of maintaining the directory described in clause (i)(I).\n**(C) Effect of failure to designate**\nThere shall be established a presumption that a provider of an online service described in subparagraph (A)(i) has not undertaken a good faith effort to comply with this subsection if the provider has failed to register a designated agent under this paragraph by the later of\u2014\n**(i)**\nthe date that is 90 days after the effective date of this section; or\n**(ii)**\nthe date that is 90 days after the date on which the provider becomes a provider described in subparagraph (A)(i).\n**(3) Elements of notification**\nTo be effective under this subsection, a notification of a claimed violation of the right described in subsection (b) shall be a written communication provided to the designated agent registered under this subsection with respect to the applicable provider of an online service that includes the following:\n**(A)**\nA physical or electronic signature of the right holder, an individual or entity authorized to act on behalf of the right holder, or an eligible plaintiff under subsection (e)(1).\n**(B)**\nIdentification of the individual, the voice or visual likeness of whom is at issue with respect to an unauthorized digital replica or a product or service described in subsection (c)(2)(B).\n**(C)**\nIdentification of the material containing an unauthorized digital replica or a product or service described in subsection (c)(2)(B), including information sufficient to allow the provider to locate the identified material.\n**(D)**\nInformation reasonably sufficient to permit the provider to contact the notifying party, such as an address, telephone number, and email address.\n**(E)**\nA statement that the notifying party believes in good faith that\u2014\n**(i)**\nthe material is an unauthorized use of a digital replica or a product or service described in subsection (c)(2)(B); and\n**(ii)**\nthe exclusions under subsection (c)(5) do not apply.\n**(F)**\nIf not the right holder or an eligible plaintiff under subsection (e)(1), a statement, under penalty of perjury, that the notifying party has the authority to act on behalf of the right holder.\n**(G)**\nFor the purposes of paragraph (1)(B), information reasonably sufficient to\u2014\n**(i)**\nidentify the reference or link to the material or activity claimed to be or containing an unauthorized digital replica, or a product or service described in subsection (c)(2)(B), that is to be removed or to which access is to be disabled; and\n**(ii)**\npermit the provider to locate the reference or link described in clause (i).\n**(4) Elements of counter-notification**\nTo be effective under this subsection, a counter-notification with respect to a notification provided under paragraph (3) shall be a written communication that satisfies the following:\n**(A)**\nThe counter-notification is provided\u2014\n**(i)**\nto the designated agent of the online service provider to which that notification was submitted under paragraph (3); and\n**(ii)**\nby the party that placed the applicable material on the online service.\n**(B)**\nThe counter notification includes the following:\n**(i)**\nA physical signature, witnessed or attested to in person by a licensed notary public, of the individual or entity that placed the applicable material on the online service.\n**(ii)**\nAn identification of the material that has been removed or to which access has been disabled and the location at which the material appeared before the material was removed or access to the material was disabled.\n**(iii)**\nInformation that is reasonably sufficient to permit the provider of the online service and the individual or entity that provided the notification under paragraph (3) to contact the party providing the counter-notification, including an address, telephone number, and email address.\n**(iv)**\nA statement made under penalty of perjury that the party providing the counter-notification has a good faith belief that the applicable material was removed, or access to that material was disabled, as a result of mistake or misidentification of the material to be removed or access to which was to be disabled, which shall include a specific assertion by the party providing the counter-notification that such material\u2014\n**(I)**\nis not a digital replica;\n**(II)**\nis an authorized digital replica; or\n**(III)**\nis an unauthorized digital replica that satisfies an exclusion under paragraph (4) or (5) of subsection (c), or any other requirements with respect to a valid legal defense, which shall include a succinct explanation of how such material satisfies the applicable exclusion or requirement.\n**(v)**\nA statement that the individual or entity described in clause (i)\u2014\n**(I)**\nconsents to the jurisdiction of the district court of the United States for the judicial district in which the address provided under clause (iii) is located (or, if that address is outside of the United States, for any judicial district of the United States in which the provider may be found); and\n**(II)**\nwill accept service of process from\u2014\n**(aa)**\nthe individual or entity that provided notification under paragraph (3); or\n**(bb)**\nan agent of the individual or entity described in item (aa).\n**(5) Penalties for false or deceptive notice**\n**(A) Knowing material representations**\n**(i) In general**\nIt shall be unlawful to knowingly materially misrepresent\u2014\n**(I)**\nin a notification provided under paragraph (3)\u2014\n**(aa)**\nthat the material requested to be removed, or access to which is requested to be disabled, is an unauthorized digital replica;\n**(bb)**\nthat the exclusions under subsection (c)(5) do not apply; or\n**(cc)**\nthat an individual or entity has the authority to act on behalf of the right holder; or\n**(II)**\nin a counter-notification provided under paragraph (4)\u2014\n**(aa)**\nthat the material removed, or to which access was disabled\u2014\n(AA)\nwas removed or disabled by mistake or misidentification;\n(BB)\nis not a digital replica; or\n(CC)\nis subject to an exclusion under subsection (c)(5) or any other valid legal defense.\n**(ii) Failure to perform good faith review**\nThe failure to consider in good faith any of the issues described in clause (i)(I) before providing a notification under paragraph (3), or any of the issues described in clause (i)(II) before providing a counter-notification under paragraph (4), shall constitute a knowing material misrepresentation under this subparagraph.\n**(B) Penalties**\nIn addition to a cause of action and remedies made available under subsection (e), any individual or entity that violates subparagraph (A) of this paragraph shall be liable to the applicable right holder, the alleged violator that uploaded the applicable material, or the provider of an online service injured by the misrepresentation, for an amount equal to the greater of\u2014\n**(i)**\n$25,000 per notification provided under paragraph (3), or counter-notification provided under paragraph (4), that contains a misrepresentation described in subparagraph (A) of this paragraph; or\n**(ii)**\n**(I)**\nany actual damages incurred by the applicable right holder or alleged violator, as well as by any provider of an online service or other individual or entity injured by the misrepresentation; and\n**(II)**\nany costs and attorney\u2019s fees incurred by the applicable recipient of a notification under paragraph (3), or a counter-notification under paragraph (4), that prevails in an action alleging that the notification or counter-notification, as applicable, was false or deceptive.\n##### (e) Civil action\n**(1) Eligible plaintiffs**\nA civil action against an individual or entity that, in a manner affecting interstate commerce (or using any means or facility of interstate commerce), commits a violation of subsection (c) may be brought by\u2014\n**(A)**\nthe applicable right holder;\n**(B)**\nif the applicable right holder is an individual who is younger than 18 years of age, a parent or guardian of that individual; or\n**(C)**\nin the case of a digital replica involving a sound recording artist, any individual or entity that has, directly or indirectly, entered into\u2014\n**(i)**\na contract for the exclusive personal services of the sound recording artist as a sound recording artist; or\n**(ii)**\nan exclusive license to distribute or transmit 1 or more works that capture the audio performance of the sound recording artist.\n**(2) Limitations period**\nA civil action may not be brought under this subsection unless the civil action is commenced not later than 3 years after the date on which the party seeking to bring the civil action discovered, or with due diligence should have discovered, the applicable violation.\n**(3) Defense not permitted**\nIt shall not be a defense in a civil action brought under this subsection that the defendant displayed or otherwise communicated to the public a disclaimer stating that the applicable digital replica, or the applicable product or service described in subsection (c)(2)(B), was unauthorized or disclosed that the digital replica, product, or service was generated through the use of artificial intelligence or other technology.\n**(4) Remedies**\n**(A) In general**\nIn any civil action brought under this subsection\u2014\n**(i)**\nan individual or entity found to have committed a violation of subsection (c) shall be liable to the injured party in an amount equal to the greater of\u2014\n**(I)**\n**(aa)**\nin the case of an individual, $5,000 per work embodying the applicable unauthorized digital replica;\n**(bb)**\nin the case of a provider of an online service that has undertaken a good faith effort to implement all applicable obligations of paragraphs (1) through (4) of subsection (d), $25,000 per work embodying the applicable unauthorized digital replica;\n**(cc)**\nin the case of a provider of an online service that has not undertaken a good faith effort to implement all applicable obligations of paragraphs (1) through (4) of subsection (d), $5,000 per display, copy made, transmission, and instance of the unauthorized digital replica being made available on the online service in a sum of not more than $750,000 per work embodying the applicable unauthorized digital replica; and\n**(dd)**\nin the case of an entity that is not a provider of an online service, $25,000 per work embodying the applicable unauthorized digital replica; or\n**(II)**\nany actual damages suffered by the injured party as a result of the activity, plus any profits from the unauthorized use that are attributable to such use and are not taken into account in computing the actual damages;\n**(ii)**\nan individual or entity found to have violated subsection (c) by virtue of engaging in an activity described in subsection (c)(2)(B) shall be liable to the injured party in an amount equal to the greater of\u2014\n**(I)**\n**(aa)**\nin the case of an individual, $5,000 per product or service;\n**(bb)**\nin the case of a provider of an online service that has undertaken a good faith effort to implement all applicable obligations of paragraphs (1) through (4) of subsection (d), $25,000 per product or service;\n**(cc)**\nin the case of a provider of an online service that has not undertaken a good faith effort to implement all applicable obligations of paragraphs (1) through (4) of subsection (d), $750,000 per product or service; or\n**(dd)**\nin the case of an entity that is not a provider of an online service, $25,000 per product or service; or\n**(II)**\nany actual damages suffered by the injured party as a result of the activity, plus any profits from the unauthorized use that are attributable to such use and are not taken into account in computing the actual damages;\n**(iii)**\nthe plaintiff may seek injunctive or other equitable relief;\n**(iv)**\nin the case of willful activity in which the injured party has proven that the defendant acted with malice, fraud, knowledge, or willful avoidance of knowledge that the conduct violated the law, the court may award to the injured party punitive damages; and\n**(v)**\nif the prevailing party is\u2014\n**(I)**\nthe party bringing the action, the court shall award reasonable attorney\u2019s fees; or\n**(II)**\nthe party defending the action, the court shall award reasonable attorney\u2019s fees if the court determines that the action was not brought in good faith.\n**(B) Objectively reasonable belief**\nA provider of an online service that has designated an agent under subsection (d)(2) and has an objectively reasonable belief that material that is claimed to be an unauthorized digital replica does not qualify as a digital replica shall be liable only for actual damages under subparagraph (A) if the material is ultimately determined to be an unauthorized digital replica.\n##### (f) Subpoena To identify violator\n**(1) Request**\nA right holder, an individual or entity authorized to act on behalf of a right holder, or an eligible plaintiff under subsection (e)(1) may request the clerk of any district court of the United States to issue a subpoena to a provider of an online service for identification of an alleged violator of this section in accordance with this subsection.\n**(2) Contents of request**\nA request under paragraph (1) may be made by filing with the clerk\u2014\n**(A)**\na copy of a notification described in subsection (d)(3);\n**(B)**\na proposed subpoena; and\n**(C)**\na sworn declaration to the effect that\u2014\n**(i)**\nthe purpose of the subpoena is to obtain the identity of an individual or entity alleged to be liable under subsection (c); and\n**(ii)**\nthe information described in clause (i) will only be used for the purpose of protecting rights under this section.\n**(3) Contents of subpoena**\nA subpoena issued under this subsection shall authorize and order the provider of the applicable online service to expeditiously disclose to the party that sought the subpoena information sufficient to identify the alleged violator by virtue of the activity described in the notification to the extent that information is available to the provider of the online service.\n**(4) Basis for granting subpoena**\nIf a proposed subpoena under this subsection is in proper form, the applicable notification filed satisfies the requirements under subsection (d)(3), and the accompanying declaration is properly executed, the clerk shall expeditiously issue and sign the proposed subpoena and return the subpoena to the requester for delivery to the provider of the applicable online service.\n##### (g) Preemption\n**(1) In general**\nThe rights established under this Act shall preempt any cause of action under State law for the protection of an individual\u2019s voice and visual likeness rights in connection with a digital replica, as defined in this Act, in an expressive work.\n**(2) Rule of construction**\nNotwithstanding paragraph (1), nothing in this Act may be construed to preempt\u2014\n**(A)**\ncauses of action under State statutes or common law in existence, as of January 2, 2025, regarding a digital replica;\n**(B)**\ncauses of action under State statutes specifically regulating a digital replica depicting sexually explicit conduct, as defined in section 2256(2)(A) of title 18, United States Code, or an election-related digital replica; or\n**(C)**\ncauses of action under State statutes or common law in existence, as of January 2, 2025, for the distributing, importing, transmitting, or otherwise making available to the public a product or service capable of producing 1 or more digital replicas.\n##### (h) Rules of construction\n**(1) Laws pertaining to intellectual property**\nThis section shall be considered to be a law pertaining to intellectual property for the purposes of section 230(e)(2) of the Communications Act of 1934 ( 47 U.S.C. 230(e)(2) ).\n**(2) No duty to monitor**\nExcept as expressly provided in subsection (d)(1)(B)(ii), nothing in this section may be construed to require the provider of an online service to\u2014\n**(A)**\nmonitor the online service for, or affirmatively seek facts about, any digital replica; or\n**(B)**\ngain access to material.\n##### (i) Severability\nIf any provision of this section, or the application of a provision of this section, is held to be invalid, the validity of the remainder of this section, and the application of that provision to other individuals, entities, and circumstances, shall not be affected by that holding.\n##### (j) Retroactive effect\n**(1) Liabilities**\nLiability under this section shall apply only to\u2014\n**(A)**\nconduct occurring after the date of enactment of this Act; and\n**(B)**\nin the case of conduct covered by a license or contract, a license or contract that is executed after the date of enactment of this Act.\n**(2) Digital replication right**\nThe right granted under subsection (b)\u2014\n**(A)**\nshall apply to any individual, regardless of whether the individual dies before, on, or after the date of enactment of this Act; and\n**(B)**\nin the case of a right holder who has died before the date of enactment of this Act, shall vest in the executors, heirs, assignees, or devisees of the right holder.\n##### (k) Effective date\nThis Act shall take effect on the date that is 180 days after the date of enactment of this Act.",
      "versionDate": "2026-05-20",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4591is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "NO FAKES Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-30T04:53:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "NO FAKES Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-30T04:53:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Nurture Originals, Foster Art, and Keep Entertainment Safe Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-30T04:53:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to protect intellectual property rights in the voice and visual likeness of individuals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-30T04:48:26Z"
    }
  ]
}
```
