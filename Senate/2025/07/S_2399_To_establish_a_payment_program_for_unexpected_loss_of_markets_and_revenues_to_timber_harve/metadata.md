# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2399?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2399
- Title: Loggers Economic Assistance and Relief Act
- Congress: 119
- Bill type: S
- Bill number: 2399
- Origin chamber: Senate
- Introduced date: 2025-07-23
- Update date: 2025-12-05T21:56:37Z
- Update date including text: 2025-12-05T21:56:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in Senate
- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (Sponsor introductory remarks on measure: CR S4626)
- Latest action: 2025-07-23: Introduced in Senate

## Actions

- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (Sponsor introductory remarks on measure: CR S4626)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2399",
    "number": "2399",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "C001035",
        "district": "",
        "firstName": "Susan",
        "fullName": "Sen. Collins, Susan M. [R-ME]",
        "lastName": "Collins",
        "party": "R",
        "state": "ME"
      }
    ],
    "title": "Loggers Economic Assistance and Relief Act",
    "type": "S",
    "updateDate": "2025-12-05T21:56:37Z",
    "updateDateIncludingText": "2025-12-05T21:56:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (Sponsor introductory remarks on measure: CR S4626)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T16:34:12Z",
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
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-07-23",
      "state": "ME"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "VT"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2399is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2399\nIN THE SENATE OF THE UNITED STATES\nJuly 23, 2025 Ms. Collins (for herself, Mr. King , Mr. Welch , and Mrs. Shaheen ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo establish a payment program for unexpected loss of markets and revenues to timber harvesting and timber hauling businesses due to major disasters, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Loggers Economic Assistance and Relief Act .\n#### 2. Payment program for timber harvesting and timber hauling businesses\n##### (a) Definitions\nIn this section:\n**(1) Eligible entity**\nThe term eligible entity means any timber harvesting business or timber hauling business that harvested or hauled unrefined timber products in the previous calendar year.\n**(2) Major disaster**\nThe term major disaster \u2014\n**(A)**\nhas the meaning given the term in section 102(2) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5122(2) ); and\n**(B)**\nincludes an insect infestation declared a major disaster pursuant to such Act.\n**(3) Gross revenue**\nThe term gross revenue means the gross revenue generated by an eligible entity from timber harvesting or timber hauling services within the normal range of operation of the eligible entity, as determined by the Secretary.\n**(4) Secretary**\nThe term Secretary means the Secretary of Agriculture, acting through the Administrator of the Farm Service Agency.\n##### (b) Payments\nThe Secretary shall make payments in accordance with this section to eligible entities that as a result of a major disaster experienced a loss of not less than 10 percent in gross revenue in a 30-day period or quarter of a calendar year, as compared to the gross revenue of the eligible entity during the same 30-day period or quarter of the previous calendar year.\n##### (c) Amount of payment\nThe amount of a payment made to an eligible entity under subsection (b) shall be equal to 10 percent of the gross revenue of the eligible entity during the applicable period under subsection (b).\n##### (d) Allowable use\nThe Secretary shall only make a payment under subsection (b) to an eligible entity that certifies to the Secretary that the payment will be used only for operating expenses.\n##### (e) Report\nNot later than 180 days after the date of enactment of this Act, and annually thereafter, the Secretary shall submit to the Committee on Agriculture, Nutrition, and Forestry of the Senate and the Committee on Agriculture of the House of Representatives a report describing the payments made under this section, including\u2014\n**(1)**\nthe identity of each recipient of a payment; and\n**(2)**\nthe amount of each payment provided to each recipient described in paragraph (1).\n##### (f) Regulations\n**(1) In general**\nExcept as otherwise provided in this section, not later than 30 days after the date of enactment of this Act, the Secretary shall prescribe such regulations as are necessary to carry out this section.\n**(2) Procedure**\nThe promulgation of regulations under, and administration of, this section shall be made without regard to\u2014\n**(A)**\nthe notice and comment provisions of section 553 of title 5, United States Code; and\n**(B)**\nchapter 35 of title 44, United States Code (commonly known as the Paperwork Reduction Act ).\n##### (g) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $50,000,000 for each of fiscal years 2025 through 2029.",
      "versionDate": "2025-07-23",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-07-23",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "4665",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Loggers Economic Assistance and Relief Act",
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
        "name": "Emergency Management",
        "updateDate": "2025-09-16T22:32:25Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2399is.xml"
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
      "title": "Loggers Economic Assistance and Relief Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-05T04:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Loggers Economic Assistance and Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T04:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a payment program for unexpected loss of markets and revenues to timber harvesting and timber hauling businesses due to major disasters, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T04:48:24Z"
    }
  ]
}
```
