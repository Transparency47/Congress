# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/651?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/651
- Title: Spectrum Pipeline Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 651
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2026-01-28T19:17:34Z
- Update date including text: 2026-01-28T19:17:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/651",
    "number": "651",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "A000372",
        "district": "12",
        "firstName": "Rick",
        "fullName": "Rep. Allen, Rick W. [R-GA-12]",
        "lastName": "Allen",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Spectrum Pipeline Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-28T19:17:34Z",
    "updateDateIncludingText": "2026-01-28T19:17:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T15:04:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "ID"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr651ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 651\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Mr. Allen introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require the Federal Communications Commission to auction spectrum in the band between 1.3 gigahertz and 13.2 gigahertz, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Spectrum Pipeline Act of 2025 .\n#### 2. Identification of spectrum for reallocation and auction\n##### (a) Definitions\nIn this section:\n**(1) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Commerce, Science, and Transportation of the Senate; and\n**(B)**\nthe Committee on Energy and Commerce of the House of Representatives.\n**(2) Assistant Secretary**\nThe term Assistant Secretary means the Assistant Secretary of Commerce for Communications and Information.\n**(3) Commission**\nThe term Commission means the Federal Communications Commission.\n**(4) Covered band**\nThe term covered band means the band of frequencies between 1.3 gigahertz and 13.2 gigahertz.\n**(5) Federal entity**\nThe term Federal entity has the meaning given the term in section 113(l) of the National Telecommunications and Information Administration Organization Act ( 47 U.S.C. 923(l) ).\n**(6) Full-power commercial licensed use cases**\nThe term full-power commercial licensed use cases means flexible use wireless broadband services with base station power levels sufficient for high-power, high-density, and wide-area commercial mobile services, consistent with the service rules under part 27 of title 47, Code of Federal Regulations, or any successor regulations, for wireless broadband deployments throughout the covered band.\n##### (b) Identification for reallocation\n**(1) In general**\nThe Assistant Secretary, in consultation with the Commission, shall identify not less than 2500 megahertz of spectrum in the covered band, that as of the date of enactment of this Act is allocated for Federal use or for shared Federal and non-Federal use, for reallocation for non-Federal use, shared Federal and non-Federal use, or a combination thereof, including not less than 1250 megahertz for full-power commercial licensed use cases.\n**(2) Schedule**\nThe Assistant Secretary shall identify the spectrum under paragraph (1) according to the following schedule:\n**(A)**\nNot later than 2 years after the date of enactment of this Act, the Assistant Secretary shall identify not less than 1250 megahertz of spectrum.\n**(B)**\nNot later than 5 years after the date of enactment of this Act, the Assistant Secretary shall identify any remaining spectrum required to be identified under paragraph (1) after compliance with subparagraph (A) of this paragraph.\n##### (c) Auctions\n**(1) In general**\nWith respect to the spectrum identified for reallocation under subsection (b) for commercial licensed use, the Commission shall grant licenses through systems of competitive bidding for not less than 1250 megahertz of the spectrum for full-power commercial licensed use cases.\n**(2) Schedule**\nThe Commission shall auction the spectrum under paragraph (1) according to the following schedule:\n**(A)**\nNot later than 3 years after the date of enactment of this Act, the Commission shall complete 1 or more systems of competitive bidding for not less than 600 megahertz of the spectrum.\n**(B)**\nNot later than 6 years after the date of enactment of this Act, the Commission shall complete 1 or more systems of competitive bidding for any remaining spectrum required to be auctioned under paragraph (1) after compliance with subparagraph (A) of this paragraph.\n##### (d) Unlicensed use\nNot later than 2 years after the date of enactment of this Act, the Commission shall make available on an unlicensed basis not less than 125 megahertz of the spectrum in the covered band.\n##### (e) Licensed or unlicensed use\nNot later than 8 years after the date of enactment of this Act, the Commission shall make available for use on a licensed or unlicensed basis any remaining spectrum that is\u2014\n**(1)**\nidentified under subsection (b); and\n**(2)**\nnot\u2014\n**(A)**\nauctioned under subsection (c); or\n**(B)**\nmade available on an unlicensed basis under subsection (d).\n##### (f) Auction proceeds To cover 110 percent of Federal relocation or sharing costs\nNothing in this section shall be construed to relieve the Commission from the requirements under section 309(j)(16)(B) of the Communications Act of 1934 ( 47 U.S.C. 309(j)(16)(B) ).\n##### (g) Auction authority\nSection 309(j)(11) of the Communications Act of 1934 ( 47 U.S.C. 309(j)(11) ) is amended\u2014\n**(1)**\nby striking grant a license or permit under this subsection shall expire March 9, 2023 and inserting complete a system of competitive bidding under this subsection shall expire September 30, 2027 ;\n**(2)**\nby striking and with respect to and inserting with respect to ; and\n**(3)**\nby inserting before the period at the end the following: , and with respect to the electromagnetic spectrum in the covered band (as defined in section 2(a) of the Spectrum Pipeline Act of 2025 ), such authority shall expire on the date that is 8 years after the date of enactment of that Act .\n##### (h) Reporting requirements and quarterly briefings\n**(1) NTIA progress report on spectrum identification**\n**(A) In general**\nOn each date as of which the Assistant Secretary, in consultation with the Commission, has identified the quantity of spectrum required under subparagraph (A) or (B), respectively, of subsection (b)(2), the Assistant Secretary shall submit to the appropriate committees of Congress a report detailing the findings and conclusions that the Assistant Secretary used to support the identification.\n**(B) Contents**\nThe Assistant Secretary shall include in each report submitted under subparagraph (A)\u2014\n**(i)**\nan analysis of the spectrum identified; and\n**(ii)**\nthe Federal entities with which the Assistant Secretary coordinated regarding the spectrum identified.\n**(C) Form of report**\nEach report required under subparagraph (A) shall be submitted in unclassified form, but may contain a classified annex.\n**(2) NTIA and FCC reports on reallocation of spectrum identified**\n**(A) Initial progress report**\nNot later than 1 year after the date of enactment of this Act, the Assistant Secretary, in consultation with the Commission, shall submit to the appropriate committees of Congress a report on the progress of the Assistant Secretary in identifying spectrum in the covered band for reallocation under subsection (b) that includes\u2014\n**(i)**\nan assessment of the operations of the Federal entities and non-Federal entities that operate in the spectrum in the covered band; and\n**(ii)**\na preliminary analysis of which portions of the covered band are being considered for reallocation in accordance with subsection (b)(1).\n**(B) Reports on 2 tranches of identified spectrum**\nNot later than 60 days after each date as of which the Assistant Secretary, in consultation with the Commission, has identified the quantity of spectrum required under subparagraph (A) or (B), respectively, of subsection (b)(2), the Assistant Secretary, in consultation with the Commission, shall submit to the appropriate committees of Congress a report that includes\u2014\n**(i)**\nan assessment of the operations of the Federal entities and non-Federal entities that operate in the applicable spectrum, current as of the date of the submission of the report;\n**(ii)**\nthe steps the President has taken to begin the process of withdrawing or modifying the assignments of Federal entities in the covered band as necessary for the Commission to begin and complete the systems of competitive bidding under subsection (c);\n**(iii)**\nan estimate of the funding required for the relocation or sharing costs (as defined in section 113(g)(3) of the National Telecommunications and Information Administration Organization Act ( 47 U.S.C. 923(g)(3) )) expected to be incurred by the Federal entities described in clause (ii) in connection with the reallocation of the applicable spectrum; and\n**(iv)**\nsteps the Assistant Secretary is taking to ensure global harmonization with the spectrum to be reallocated.\n**(C) Form of report**\nEach report required under this paragraph shall be submitted in unclassified form, but may contain a classified annex.\n**(3) Annual briefings**\n**(A) In general**\nNot later than 1 year after the date of enactment of this Act, and annually thereafter until the date that is 10 years after such date of enactment, the Assistant Secretary and the Chairman of the Commission shall provide the appropriate committees of Congress with a briefing on the progress of the Assistant Secretary and the Chairman in complying with the requirements of this section.\n**(B) Contents**\nThe Assistant Secretary and the Chairman of the Commission shall include in each briefing under subparagraph (A)\u2014\n**(i)**\nan update on the specific frequencies of spectrum under consideration or that have been identified to meet the requirements of subsection (b);\n**(ii)**\nan explanation of the Federal entities and non-Federal entities that operate on the frequencies described in clause (i) and the specific services or systems utilized by those entities on those frequencies;\n**(iii)**\nthe extent to which Federal entities are cooperating with the efforts of the Assistant Secretary and the Chairman of the Commission to comply with the requirements of this Act;\n**(iv)**\nan update on the progress of the systems of competitive bidding required by subsection (c); and\n**(v)**\nany additional information related to compliance with this Act by the Assistant Secretary and the Chairman.\n**(C) Form of briefing**\nAny classified information that would otherwise be provided in a briefing under subparagraph (A) shall be provided in a separate classified briefing.\n#### 3. Spectrum Relocation Fund modernization\n##### (a) Congressional notification timelines\nSection 118 of the National Telecommunications and Information Administration Organization Act ( 47 U.S.C. 928 ) is amended\u2014\n**(1)**\nin subsection (d)(2)\u2014\n**(A)**\nin subparagraph (C), by striking 30 days and inserting 15 days ; and\n**(B)**\nin the matter following subparagraph (C), by striking 30 days and inserting 15 days ;\n**(2)**\nin subsection (f)(2)(B)(iv), by striking 30 days and inserting 15 days ; and\n**(3)**\nin subsection (g)(2)(D)(ii), by striking 60 days and inserting 15 days .\n##### (b) Comparable capability\nSection 113(g)(3) of the National Telecommunications and Information Administration Organization Act ( 47 U.S.C. 923(g)(3) ) is amended\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nin clause (iv), by striking ; and and inserting a semicolon;\n**(B)**\nin clause (v), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(vi) the costs associated with replacing systems and equipment with state-of-the-art systems and equipment, including systems and equipment with additional functions, only if the state-of-the-art systems and equipment allow for the reallocation of significantly more valuable spectrum frequencies from Federal use to exclusive non-Federal use or to shared Federal and non-Federal use than would be reallocated if systems and equipment were replaced with comparable systems and equipment or systems and equipment with incidental increases in functionality, provided the costs would not jeopardize the ability of the Assistant Secretary, in consultation with the Chair of the Commission, to reallocate eligible spectrum frequencies from Federal use to exclusive non-Federal use or to shared use. ; and\n**(2)**\nin subparagraph (B)(ii), by striking incidental .",
      "versionDate": "2025-01-23",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-02-24T19:24:52Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr651",
          "measure-number": "651",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-23",
          "originChamber": "HOUSE",
          "update-date": "2026-01-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr651v00",
            "update-date": "2026-01-28"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Spectrum Pipeline Act of 2025</strong></p><p>This bill renews the authority of the Federal Communications Commission (FCC) to auction licenses for the use of radio frequency spectrum, and requires some frequencies currently used by the federal government to be reallocated to permit use by private entities.</p><p>Specifically, the bill reauthorizes the FCC\u2019s use of competitive bidding (i.e., auctions) to grant licenses for the use of specific frequencies. (The FCC\u2019s auction authority must be renewed by Congress periodically. It expired on March 9, 2023, and has not been renewed.)</p><p>Further, the bill directs the National Telecommunications and Information Administration to identify frequencies currently designated for use by the federal government that may be reallocated to permit use by private entities either exclusively or on a shared basis. At least half of the spectrum identified for reallocation must be allocated to commercial use (including commercial wireless use), and licenses in this category must be auctioned by the FCC within a specified time frame. </p><p>A separate portion of the\u00a0spectrum must be allocated to unlicensed use. (Unlicensed frequencies are commonly used to support Wi-Fi, connected appliances, wearable consumer devices, and other electronics.)\u00a0</p><p>The bill also makes certain changes to the process for compensating federal entities that relocate to new frequencies under a spectrum reallocation plan. The bill shortens the time frame for congressional review of payments to these entities, and permits such payments to be used to cover the cost of replacing existing systems and equipment with state-of-the-art upgrades.</p>"
        },
        "title": "Spectrum Pipeline Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr651.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Spectrum Pipeline Act of 2025</strong></p><p>This bill renews the authority of the Federal Communications Commission (FCC) to auction licenses for the use of radio frequency spectrum, and requires some frequencies currently used by the federal government to be reallocated to permit use by private entities.</p><p>Specifically, the bill reauthorizes the FCC\u2019s use of competitive bidding (i.e., auctions) to grant licenses for the use of specific frequencies. (The FCC\u2019s auction authority must be renewed by Congress periodically. It expired on March 9, 2023, and has not been renewed.)</p><p>Further, the bill directs the National Telecommunications and Information Administration to identify frequencies currently designated for use by the federal government that may be reallocated to permit use by private entities either exclusively or on a shared basis. At least half of the spectrum identified for reallocation must be allocated to commercial use (including commercial wireless use), and licenses in this category must be auctioned by the FCC within a specified time frame. </p><p>A separate portion of the\u00a0spectrum must be allocated to unlicensed use. (Unlicensed frequencies are commonly used to support Wi-Fi, connected appliances, wearable consumer devices, and other electronics.)\u00a0</p><p>The bill also makes certain changes to the process for compensating federal entities that relocate to new frequencies under a spectrum reallocation plan. The bill shortens the time frame for congressional review of payments to these entities, and permits such payments to be used to cover the cost of replacing existing systems and equipment with state-of-the-art upgrades.</p>",
      "updateDate": "2026-01-28",
      "versionCode": "id119hr651"
    },
    "title": "Spectrum Pipeline Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Spectrum Pipeline Act of 2025</strong></p><p>This bill renews the authority of the Federal Communications Commission (FCC) to auction licenses for the use of radio frequency spectrum, and requires some frequencies currently used by the federal government to be reallocated to permit use by private entities.</p><p>Specifically, the bill reauthorizes the FCC\u2019s use of competitive bidding (i.e., auctions) to grant licenses for the use of specific frequencies. (The FCC\u2019s auction authority must be renewed by Congress periodically. It expired on March 9, 2023, and has not been renewed.)</p><p>Further, the bill directs the National Telecommunications and Information Administration to identify frequencies currently designated for use by the federal government that may be reallocated to permit use by private entities either exclusively or on a shared basis. At least half of the spectrum identified for reallocation must be allocated to commercial use (including commercial wireless use), and licenses in this category must be auctioned by the FCC within a specified time frame. </p><p>A separate portion of the\u00a0spectrum must be allocated to unlicensed use. (Unlicensed frequencies are commonly used to support Wi-Fi, connected appliances, wearable consumer devices, and other electronics.)\u00a0</p><p>The bill also makes certain changes to the process for compensating federal entities that relocate to new frequencies under a spectrum reallocation plan. The bill shortens the time frame for congressional review of payments to these entities, and permits such payments to be used to cover the cost of replacing existing systems and equipment with state-of-the-art upgrades.</p>",
      "updateDate": "2026-01-28",
      "versionCode": "id119hr651"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr651ih.xml"
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
      "title": "Spectrum Pipeline Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T06:23:50Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Spectrum Pipeline Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Federal Communications Commission to auction spectrum in the band between 1.3 gigahertz and 13.2 gigahertz, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:18:41Z"
    }
  ]
}
```
