# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4403?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4403
- Title: Clear Skies Act
- Congress: 119
- Bill type: HR
- Bill number: 4403
- Origin chamber: House
- Introduced date: 2025-07-15
- Update date: 2026-04-02T21:01:46Z
- Update date including text: 2026-04-02T21:01:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-15: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-07-15: Introduced in House

## Actions

- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-15",
    "latestAction": {
      "actionDate": "2025-07-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4403",
    "number": "4403",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "G000596",
        "district": "14",
        "firstName": "Marjorie",
        "fullName": "Rep. Greene, Marjorie Taylor [R-GA-14]",
        "lastName": "Greene",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Clear Skies Act",
    "type": "HR",
    "updateDate": "2026-04-02T21:01:46Z",
    "updateDateIncludingText": "2026-04-02T21:01:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-15",
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
      "actionDate": "2025-07-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-15",
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
          "date": "2025-07-15T14:05:00Z",
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
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "TN"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "WI"
    },
    {
      "bioguideId": "M001184",
      "district": "4",
      "firstName": "Thomas",
      "fullName": "Rep. Massie, Thomas [R-KY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Massie",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "KY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4403ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4403\nIN THE HOUSE OF REPRESENTATIVES\nJuly 15, 2025 Ms. Greene of Georgia introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo prohibit weather modification within the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Clear Skies Act .\n#### 2. Prohibition of weather modification\n##### (a) In general\nWhoever, in any circumstance described in subsection (b), knowingly conducts weather modification in the United States, including the territories and possessions of the United States, shall be subject to the penalties described in subsection (c).\n##### (b) Circumstances described\nFor the purposes of subsection (a), the circumstances described in this subsection are that\u2014\n**(1)**\nthe defendant traveled in interstate or foreign commerce, or traveled using a means, channel, facility, or instrumentality of interstate or foreign commerce, in furtherance of or in connection with the conduct described in subsection (a);\n**(2)**\nthe defendant used a means, channel, facility, or instrumentality of interstate or foreign commerce in furtherance of or in connection with the conduct described in subsection (a);\n**(3)**\nthe defendant transmitted in interstate or foreign commerce any communication relating to or in furtherance of the conduct described in subsection (a) using any means, channel, facility, or instrumentality of interstate or foreign commerce or in or affecting interstate or foreign commerce by any means or in any manner, including by computer, mail, wire, or electromagnetic transmission;\n**(4)**\nthe conduct described in subsection (a) occurred within the special maritime and territorial jurisdiction of the United States, the special aircraft jurisdiction of the United States, or any territory or possession of the United States; or\n**(5)**\nthe conduct described in subsection (a) otherwise occurred in or affected interstate or foreign commerce.\n##### (c) Penalties\n**(1) Criminal penalty**\nWhoever violates subsection (a) shall be fined not more than $100,000 for each violation, imprisoned not more than 5 years, or both.\n**(2) Civil penalty**\nThe Administrator of the Environmental Protection Agency may, in coordination with the Administrator of the Federal Aviation Administration, impose a civil penalty of not more than $10,000 for each violation of subsection (a), in addition to any other penalties provided by law.\n**(3) Repeat violations**\nEach instance of injection, release, emission, or dispersal under subsection (a) shall constitute a separate violation of such section.\n#### 3. Reporting and investigation\n##### (a) Public reporting\n**(1) Establishment of system**\nThe Administrator of the Environmental Protection Agency, in coordination with the Administrator of the Federal Aviation Administration and the Administrator of the National Oceanic and Atmospheric Administration, shall establish a system for the public to report suspected violations of section 2.\n**(2) Submission of reports**\nSuch system may collect reports via telephone, email, mail, or an online portal.\n**(3) Publication of reports**\nThe Administrator of the Environmental Protection Agency shall make publicly available on the website of the Environmental Protection Agency any reports collected by such system under this subsection.\n##### (b) Investigation\n**(1) In general**\nThe Administrator of the Environmental Protection Agency shall investigate suspected violations of section 2 reported under subsection (a) that the Administrator determines warrant further review.\n**(2) Determination**\n**(A) Requirement**\nFor any suspected violation investigated under paragraph (1), the Administrator shall determine whether a violation of section 2 has occurred.\n**(B) Coordination**\nIn determining whether a violation of section 2 occurred, the Administrator of the Environmental Protection Agency may coordinate with the Secretary of Agriculture, the Secretary of the Interior, the Administrator of the Federal Aviation Administration, the Administrator of the National Aeronautics and Space Administration, the Administrator of the National Oceanic and Atmospheric Administration, or the head of any other Federal agency that the Administrator of the Environmental Protection Agency determines to be relevant, to verify the nature of any activities described in a report submitted under subsection (a).\n##### (c) Referral to DOJ\nThe Administrator of the Environmental Protection Agency shall refer a suspected violation that the Administrator determines to have occurred under subsection (b)(2) to the Attorney General of the United States for further action.\n#### 4. Repeal of existing authorities\n##### (a) Federal statutes\nAny provision of a Federal statute authorizing or requiring weather modification, including a licensing requirement or permit for any such weather modification, is hereby repealed.\n##### (b) Federal regulations or executive orders\nAny provision of a Federal regulation or executive order authorizing or requiring weather modification, including a licensing requirement or permit for any such weather modification, is hereby nullified and shall have no force or effect.\n#### 5. Definitions\nIn this Act:\n**(1) Atmosphere**\nThe term atmosphere means the gaseous envelope surrounding the Earth, including all airspace within the territorial jurisdiction of the United States.\n**(2) Weather modification**\n**(A) In general**\nThe term weather modification means any injection, release, emission, or dispersal of a chemical, a chemical compound, or a substance, or conveyance of an apparatus, into the atmosphere for the express purpose of\u2014\n**(i)**\nproducing an artificial change in the composition, behavior, or dynamics of the atmosphere; or\n**(ii)**\naffecting the temperature, weather, climate, or intensity of sunlight.\n**(B) Examples**\nSuch term includes\u2014\n**(i)**\ngeoengineering;\n**(ii)**\ncloud seeding;\n**(iii)**\nsolar radiation modification and management; and\n**(iv)**\na release of an aerosol into the atmosphere to influence temperature, precipitation, or the intensity of sunlight.\n#### 6. Effective date\nThis Act shall take effect 90 days after the date of enactment of this Act.",
      "versionDate": "2025-07-15",
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
        "actionDate": "2026-02-09",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Transportation and Infrastructure, and Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "7452",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Air Quality Act",
      "type": "HR"
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
        "name": "Environmental Protection",
        "updateDate": "2025-07-31T12:09:54Z"
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
      "date": "2025-07-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4403ih.xml"
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
      "title": "Clear Skies Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T02:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Clear Skies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-23T02:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit weather modification within the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-23T02:03:29Z"
    }
  ]
}
```
