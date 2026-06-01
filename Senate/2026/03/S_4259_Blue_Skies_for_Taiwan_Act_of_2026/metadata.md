# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4259?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4259
- Title: Blue Skies for Taiwan Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4259
- Origin chamber: Senate
- Introduced date: 2026-03-26
- Update date: 2026-04-14T11:03:26Z
- Update date including text: 2026-04-14T11:03:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in Senate
- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2026-03-26: Introduced in Senate

## Actions

- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4259",
    "number": "4259",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Blue Skies for Taiwan Act of 2026",
    "type": "S",
    "updateDate": "2026-04-14T11:03:26Z",
    "updateDateIncludingText": "2026-04-14T11:03:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T20:59:52Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "TX"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "UT"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4259is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4259\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2026 Mr. Merkley (for himself, Mr. Cruz , and Mr. Curtis ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo promote the development, production, and deployment of secure and resilient Unmanned Aerial Systems (UAS) to enhance United States national security and support the defense and resilience of Taiwan in the Indo-Pacific Region.\n#### 1. Short title\nThis Act may be cited as the Blue Skies for Taiwan Act of 2026 .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Relations, the Committee on Armed Services, the Committee on the Budget, and the Committee on Appropriations of the Senate; and\n**(B)**\nthe Committee on Foreign Affairs, the Committee on Armed Services, the Committee on the Budget, and the Committee on Appropriations of the House of Representatives.\n**(2) Blue UAS**\nThe term Blue UAS refers to UAS components and systems that comply with Defense Contract Management Agency\u2019s Blue UAS program and its associated list.\n#### 3. Findings\nCongress makes the following findings:\n**(1)**\nTaiwan is a longstanding and vital democratic partner whose security is central to United States strategic interests and regional stability in the Indo-Pacific region.\n**(2)**\nThe People\u2019s Republic of China (PRC) is increasingly employing gray-zone tactics, including routine use of unmanned aerial systems and other low-cost platforms, to pressure Taiwan and undermine its security.\n**(3)**\nAs set forth in the Taiwan Relations Act of 1979 ( Public Law 96\u20138 ), it is United States policy to maintain its capacity to resist any resort to force or other forms of coercion against Taiwan and provide Taiwan with arms of a defensive nature.\n**(4)**\nAs set forth in the Taiwan Enhanced Resilience Act (subtitle A of title XII of Public Law 117\u2013263 ), it is the sense of Congress that the United States should support Taiwan\u2019s acquisition and employment of capabilities that advance asymmetric strategies.\n**(5)**\nThe vast majority of commercially available UAS contain PRC-sourced components, creating significant cybersecurity, supply chain, and operational risks for both Taiwan and the United States.\n**(6)**\nTaiwan is well-positioned to develop and produce UAS components and systems but faces challenges in competing with PRC commercial companies, accessing capital, and meeting United States certification and cybersecurity requirements.\n**(7)**\nThe United States should support UAS supply chain development in Taiwan to strengthen Taiwan\u2019s asymmetric defense posture and expand United States access to secure, PRC-independent UAS components and systems.\n**(8)**\nThe Army Organic Industrial Base, including its arsenals, depots, and ammunition plants, is undergoing modernization to support emerging technologies and may provide opportunities to support the testing and sustainment of unmanned aerial systems and related components in coordination with allies and partners.\n#### 4. Blue UAS Working Group\n##### (a) Establishment\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State, in coordination with the Secretary of Defense, shall establish a Blue UAS working group, leveraging existing workstreams and expanding scope as needed, inclusive of government, industry, and academic experts, to\u2014\n**(1)**\nassess Taiwan\u2019s domestic drone production capacity, including research and development, legal and regulatory frameworks, testing, certification, and production capacities for dual-use drones;\n**(2)**\nevaluate opportunities for public-private partnerships between the United States and Taiwan for co-development and co-production of UAS systems and components, including pilot programs;\n**(3)**\nidentify barriers to the inclusion of Taiwan-manufactured components and systems manufactured in Blue UAS programs;\n**(4)**\nidentify regulatory, export-control, and certification barriers that impede Taiwan\u2019s participation in Blue UAS programs;\n**(5)**\nprovide recommendations to expand and improve incorporation of Taiwanese suppliers into Blue UAS programs;\n**(6)**\nidentify specific UAS components or systems that could be integrated into Blue UAS programs within 12 to 24 months;\n**(7)**\nanalyze opportunities and impediments to including Taiwan in Replicator programs and similar initiatives; and\n**(8)**\nassess opportunities for collaboration with the Army Organic Industrial Base, including its arsenals, depots, and ammunition plants, to support the testing, evaluation, production, maintenance, and sustainment of Blue UAS components and systems, including those co-developed or co-produced with Taiwan.\n##### (b) Reporting\nNot later than one year after the date of the enactment of this Act, and annually thereafter for three years, the Working Group shall submit to the appropriate congressional committees an unclassified report on its activities, including findings, recommendations, timelines, resource needs, and potential funding mechanisms, with a classified appendix as necessary.\n#### 5. Cooperative framework with allies\n##### (a) In general\nThe Secretary of State, in coordination with the Secretary of Defense, shall establish a cooperative framework, drawing on the Partnership for Indo-Pacific Industrial Resilience (PIPIR), among the United States, Taiwan, and regional allies and global partners to promote secure, PRC-independent UAS supply chains and enhance interoperability.\n##### (b) Elements\nThe cooperative framework shall include\u2014\n**(1)**\nsupport regional allies in the acquisition of Blue UAS components or systems from Taiwan in lieu of PRC-sourced components; and\n**(2)**\nfast-track Blue UAS certification for components co-developed or co-produced by Taiwan and regional allies.\n#### 6. Fast-track certification\n##### (a) In general\nThe Secretary of State, in coordination with the Secretary of Defense, shall develop a fast-track process for Blue UAS companies in Taiwan to obtain Blue UAS certification.\n##### (b) Elements\nThe fast-track certification process shall include the following procedures:\n**(1)**\nExpedited export control reviews and licensing for Taiwan drone and drone component manufacturers, including streamlined technical reviews for components with no PRC-connected subcomponents.\n**(2)**\nA fast-track certification procedure for Taiwanese manufacturers, including reciprocal testing arrangements or recognition of equivalent Taiwan cybersecurity standards where appropriate.\n#### 7. Authorization of appropriations\nThere are hereby authorized to be appropriated such sums as may be necessary to carry out the provisions of this Act.\n#### 8. Rules of construction\nNothing in this Act shall be construed\u2014\n**(1)**\nto alter United States policy towards Taiwan as codified in the Taiwan Relations Act of 1979 ( Public Law 96\u20138 ); and\n**(2)**\nto alter the United States Government\u2019s position with respect to the international status of Taiwan.",
      "versionDate": "2026-03-26",
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
        "name": "International Affairs",
        "updateDate": "2026-04-13T21:11:48Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4259is.xml"
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
      "title": "Blue Skies for Taiwan Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-14T11:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Blue Skies for Taiwan Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-09T02:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to promote the development, production, and deployment of secure and resilient Unmanned Aerial Systems (UAS) to enhance United States national security and support the defense and resilience of Taiwan in the Indo-Pacific Region.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-09T02:18:23Z"
    }
  ]
}
```
