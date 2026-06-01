# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4453?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4453
- Title: LINK Act
- Congress: 119
- Bill type: S
- Bill number: 4453
- Origin chamber: Senate
- Introduced date: 2026-04-30
- Update date: 2026-05-29T15:47:49Z
- Update date including text: 2026-05-29T15:47:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in Senate
- 2026-04-30 - IntroReferral: Introduced in Senate
- 2026-04-30 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2026-04-30: Introduced in Senate

## Actions

- 2026-04-30 - IntroReferral: Introduced in Senate
- 2026-04-30 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4453",
    "number": "4453",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "S001150",
        "district": "",
        "firstName": "Adam",
        "fullName": "Sen. Schiff, Adam B. [D-CA]",
        "lastName": "Schiff",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "LINK Act",
    "type": "S",
    "updateDate": "2026-05-29T15:47:49Z",
    "updateDateIncludingText": "2026-05-29T15:47:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T17:08:11Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4453is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4453\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2026 Mr. Schiff (for himself and Mr. Ricketts ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo require the Secretary of Agriculture and the Secretary of the Interior to ensure that the information technology and cybersecurity and information security systems of the Department of Agriculture and the Department of the Interior are interoperable, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the USDA\u2013DOI Linking Information Networks for Knowledge-sharing Act or the LINK Act .\n#### 2. Interoperability of information technology and cybersecurity and information security systems of the Department of Agriculture and the Department of the Interior\n##### (a) Definition of Secretary\nIn this section, the term Secretary means the Secretary of Agriculture.\n##### (b) Coordination required\n**(1) In general**\nThe Secretary and the Secretary of the Interior shall coordinate with each other to ensure that the information technology and cybersecurity and information security systems of the Department of Agriculture and the Department of the Interior, respectively, are interoperable to allow for the sharing between the Secretary and the Secretary of the Interior of information with respect to covered activities of the Department of Agriculture and the Department of the Interior, respectively, described in paragraph (2), excluding any Tribal proprietary data, sensitive cave location data, or other sensitive or proprietary information, as designated by law (including regulations).\n**(2) Description of covered activities**\nThe covered activities referred to in paragraph (1) are\u2014\n**(A)**\nFederal land management activities, with an emphasis on activities that would leverage existing integration efforts and capabilities, such as wildfire operations;\n**(B)**\ndisaster and emergency preparedness and response activities; and\n**(C)**\nprocurement, aviation management, personnel and workforce management, and other business system activities relating to the conduct of the activities described in subparagraphs (A) and (B).\n**(3) Applicable law**\nIn carrying out paragraph (1), the Secretary and the Secretary of the Interior shall comply with applicable Federal information technology system laws, including subtitle III of title 40 and chapter 35 of title 44, United States Code.\n**(4) Consultation; tribal data sovereignty**\nIn carrying out paragraph (1), the Secretary and the Secretary of the Interior shall\u2014\n**(A)**\nconsult with applicable Indian Tribes; and\n**(B)**\nprovide appropriate protections for Tribal data sovereignty.\n##### (c) Joint interoperability implementation plan\n**(1) Development**\nAs soon as practicable after the date of enactment of this Act and in consultation with firefighters, the Secretary and the Secretary of the Interior shall jointly develop an interoperability implementation plan for the Department of Agriculture and the Department of the Interior to enable the sharing between the Secretary and the Secretary of the Interior of the information described in subsection (b)(1).\n**(2) Inclusion**\nThe interoperability implementation plan developed under paragraph (1) shall include a plan for the phased retirement of siloed legacy information technology and cybersecurity and information security systems of the Department of Agriculture and the Department of the Interior that ensures that the retirement does not result in a degradation of operational capacity or mission safety.\n**(3) Implementation**\nNot later than 1 year after the date of enactment of this Act, the Secretary and the Secretary of the Interior shall implement the interoperability implementation plan developed under paragraph (1).\n##### (d) Updates to the information technology and security systems of the Department of Agriculture\nAs soon as practicable after the date of enactment of this Act, the Secretary shall update the information technology and cybersecurity and information security systems of the Department of Agriculture as necessary to enable the sharing between the Secretary and the Secretary of the Interior of the information described in subsection (b)(1), in accordance with the interoperability implementation plan developed under subsection (c).",
      "versionDate": "2026-04-30",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-05-29T15:47:49Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4453is.xml"
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
      "title": "LINK Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T03:08:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "LINK Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-15T03:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "USDA\u2013DOI Linking Information Networks for Knowledge-sharing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-15T03:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Agriculture and the Secretary of the Interior to ensure that the information technology and cybersecurity and information security systems of the Department of Agriculture and the Department of the Interior are interoperable, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-15T03:03:33Z"
    }
  ]
}
```
