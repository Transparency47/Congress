# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2048?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2048
- Title: PRC Military and Human Rights Capital Markets Sanctions Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2048
- Origin chamber: Senate
- Introduced date: 2025-06-12
- Update date: 2026-05-28T18:25:01Z
- Update date including text: 2026-05-28T18:25:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-12: Introduced in Senate
- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-06-12: Introduced in Senate

## Actions

- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2048",
    "number": "2048",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "PRC Military and Human Rights Capital Markets Sanctions Act of 2025",
    "type": "S",
    "updateDate": "2026-05-28T18:25:01Z",
    "updateDateIncludingText": "2026-05-28T18:25:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-12",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T15:39:58Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2048is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2048\nIN THE SENATE OF THE UNITED STATES\nJune 12, 2025 Mr. Ricketts introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo prohibit the purchase of certain securities from covered entities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the PRC Military and Human Rights Capital Markets Sanctions Act of 2025 .\n#### 2. Prohibition on purchase of certain securities from covered entities\n##### (a) Definitions\n**(1) Covered entity**\n**(A) In general**\nIn this section, the term covered entity means the following:\n**(i)**\nAny entity that is on the list of Specially Designated Nationals and Blocked Persons maintained by the Office of Foreign Assets Control of the Department of the Treasury, or any entity under common ownership or control with such entity.\n**(ii)**\nAny entity on the Non-SDN Chinese Military-Industrial Complex Companies List (commonly known as the NS\u2013CMIC List ) maintained by the Office of Foreign Assets Control of the Department of the Treasury pursuant to Executive Order 13959 ( 50 U.S.C. 1701 note; relating to addressing the threat from securities investments that finance communist Chinese military companies), or any entity under common ownership or control with such entity.\n**(iii)**\nAny Chinese military company included on the list maintained by the Department of Defense under section 1260H(b) of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( Public Law 116\u2013283 ; 10 U.S.C. 113 note) as of the date of the enactment of this Act, or any entity under common ownership or control with such company.\n**(iv)**\nAny Chinese entity with respect to which sanctions have been imposed under the under the Global Magnitsky Human Rights Accountability Act ( 22 U.S.C. 10101 et seq. ), or any entity under common ownership or control with such entity.\n**(v)**\nAny Chinese entity that produces goods that have been the subject of a withhold release order issued pursuant to section 307 of the Tariff Act of 1930 ( 19 U.S.C. 1307 ) during the 2-year period ending on the date of the enactment of this Act, or any entity under common ownership or control of such entity.\n**(vi)**\nAny Chinese entity included on the Entity List maintained by the Bureau of Industry and Security of the Department of Commerce and set forth in Supplement No. 4 to part 744 of title 15, Code of Federal Regulations, or any entity under common ownership or control with such entity.\n**(vii)**\nAny Chinese entity on a list maintained under clause (i), (ii), (iv), or (v) of section 2(d)(2)(B) of the Act entitled An Act to ensure that goods made with forced labor in the Xinjiang Autonomous Region of the People\u2019s Republic of China do not enter the United States market, and for other purposes , approved December 23, 2021 ( Public Law 117\u201378 ; 22 U.S.C. 6901 note) (commonly referred to as the Uyghur Forced Labor Prevention Act ), or any entity under common ownership or control with such entity.\n**(viii)**\nAny Chinese entity on the Military End-User List maintained by the Bureau of Industry and Security and set forth in Supplement No. 7 to part 744 of title 15, Code of Federal Regulations, or any entity under common ownership or control with such entity.\n**(B) Control**\nFor purposes of subparagraph (A), the term control has the meaning given the term in section 230.405 of title 17, Code of Federal Regulations.\n**(2) United states person**\nThe term United States person means\u2014\n**(A)**\na United States citizen or an alien lawfully admitted for permanent residence to the United States;\n**(B)**\nan entity organized under the laws of the United States or any jurisdiction within the United States, including a foreign branch of such an entity; or\n**(C)**\nany person in the United States.\n##### (b) Prohibition\nNot later than 90 days after the date of enactment of this Act, the President shall\u2014\n**(1)**\ncompile and maintain a single list of covered entities;\n**(2)**\nwhere possible, include in the list described in paragraph (1) a unique identification number for each covered entity, such as a Committee on Uniform Securities Identification Procedures number or a Stock Exchange Daily Official List number;\n**(3)**\nmake the list described in paragraph (1) available to the public; and\n**(4)**\npublicly identify and prohibit the purchase, sale, or holding by a United States person of a\u2014\n**(A)**\npublicly traded security issued by a covered entity;\n**(B)**\npublicly traded security that is derivative of a publicly traded security issued by a covered entity; and\n**(C)**\nsecurity that provides investment exposure to a publicly traded security issued by a covered entity.\n##### (c) Divestment required\n**(1) In general**\nNotwithstanding subsection (b), a United States person shall divest of all securities described in subsection (b)\u2014\n**(A)**\nwith respect to a security identified by the President under subsection (b) before the end of the 90-day period beginning on the date of enactment of this Act, not later than 180 days after the date of enactment of this Act; and\n**(B)**\nwith respect to a security identified by the President under subsection (b) after the end of the 90-day period beginning on the date of enactment of this Act, not later than 180 days after the date of such identification.\n**(2) Facilitating divestment transactions**\nSubsection (b) shall not apply to a United States person to the extent the person is facilitating the divestment of securities described in paragraph (1).\n##### (d) Penalties\n**(1) In general**\nA United States person that violates, attempts to violate, conspires to violate, or causes a violation of this Act shall be subject to the following penalties:\n**(A)**\nA civil penalty in an amount not to exceed the greater of\u2014\n**(i)**\n$250,000; or\n**(ii)**\nan amount that is twice the amount of the transaction that is the basis of the violation with respect to which the penalty is imposed.\n**(B)**\nWith respect to a United States person that willfully violates, willfully attempts to violate, willfully conspires to violate, or aids or abets in the commission of a violation of this Act shall be subject to a criminal penalty\u2014\n**(i)**\nof a fine of not more than $1,000,000; or\n**(ii)**\nif such United States person is an individual, a fine of not more than $1,000,000, a term of imprisonment of not more than 20 years, or both.\n**(2) Amount of a transaction defined**\nFor purposes of paragraph (1)(A)(ii), the term amount of a transaction means\u2014\n**(A)**\nwith respect to a purchase that violates this Act, the purchase price;\n**(B)**\nwith respect to a sale that violates this Act, the sale price; and\n**(C)**\nwith respect to the holding of a security that violates this Act, the fair market value of the security at the time of the violation.",
      "versionDate": "2025-06-12",
      "versionType": "Introduced in Senate"
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-07-08T13:12:54Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-12",
    "originChamber": "Senate",
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
          "measure-id": "id119s2048",
          "measure-number": "2048",
          "measure-type": "s",
          "orig-publish-date": "2025-06-12",
          "originChamber": "SENATE",
          "update-date": "2026-05-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2048v00",
            "update-date": "2026-05-28"
          },
          "action-date": "2025-06-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>PRC Military and Human Rights Capital Markets Sanctions Act of 2025</strong></p><p>This bill prohibits\u00a0U.S. persons from investing in securities issued by certain sanctioned and otherwise restricted entities, including Chinese military companies and Chinese entities sanctioned for human rights abuses or corruption.</p><p>The bill establishes divestment deadlines and criminal and civil penalties for violations of the bill.</p>"
        },
        "title": "PRC Military and Human Rights Capital Markets Sanctions Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2048.xml",
    "summary": {
      "actionDate": "2025-06-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>PRC Military and Human Rights Capital Markets Sanctions Act of 2025</strong></p><p>This bill prohibits\u00a0U.S. persons from investing in securities issued by certain sanctioned and otherwise restricted entities, including Chinese military companies and Chinese entities sanctioned for human rights abuses or corruption.</p><p>The bill establishes divestment deadlines and criminal and civil penalties for violations of the bill.</p>",
      "updateDate": "2026-05-28",
      "versionCode": "id119s2048"
    },
    "title": "PRC Military and Human Rights Capital Markets Sanctions Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-06-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>PRC Military and Human Rights Capital Markets Sanctions Act of 2025</strong></p><p>This bill prohibits\u00a0U.S. persons from investing in securities issued by certain sanctioned and otherwise restricted entities, including Chinese military companies and Chinese entities sanctioned for human rights abuses or corruption.</p><p>The bill establishes divestment deadlines and criminal and civil penalties for violations of the bill.</p>",
      "updateDate": "2026-05-28",
      "versionCode": "id119s2048"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2048is.xml"
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
      "title": "PRC Military and Human Rights Capital Markets Sanctions Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-26T06:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PRC Military and Human Rights Capital Markets Sanctions Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-26T06:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the purchase of certain securities from covered entities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-26T06:48:29Z"
    }
  ]
}
```
