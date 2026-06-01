# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2867?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2867
- Title: Farmer First Fuel Incentives Act
- Congress: 119
- Bill type: HR
- Bill number: 2867
- Origin chamber: House
- Introduced date: 2025-04-10
- Update date: 2025-12-05T21:49:59Z
- Update date including text: 2025-12-05T21:49:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-10: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-04-10: Introduced in House

## Actions

- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2867",
    "number": "2867",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M000871",
        "district": "1",
        "firstName": "Tracey",
        "fullName": "Rep. Mann, Tracey [R-KS-1]",
        "lastName": "Mann",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Farmer First Fuel Incentives Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:49:59Z",
    "updateDateIncludingText": "2025-12-05T21:49:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T13:10:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "OH"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "IL"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2867ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2867\nIN THE HOUSE OF REPRESENTATIVES\nApril 10, 2025 Mr. Mann (for himself, Ms. Kaptur , and Ms. Budzinski ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to prohibit the use of foreign feedstocks for purposes of the clean fuel production credit, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Farmer First Fuel Incentives Act .\n#### 2. Prohibition on foreign feedstocks for clean fuel production credit\n##### (a) Prohibition on foreign feedstocks\nSection 45Z(f)(1)(A) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin clause (i)(II)(bb), by striking and at the end,\n**(2)**\nin clause (ii), by striking the period at the end and inserting , and , and\n**(3)**\nby adding at the end the following new clause:\n(iii) such fuel is derived from a feedstock which was produced or grown in the United States. .\n##### (b) Effective date\nThe amendments made by this section shall apply to transportation fuel sold after December 31, 2024.\n#### 3. Determination of emissions rate\n##### (a) In general\nSection 45Z(b)(1)(B) of the Internal Revenue Code of 1986 is amended by adding at the end the following new clause:\n(iv) Exclusion of indirect land use changes Notwithstanding clauses (ii) and (iii), the lifecycle greenhouse gas emissions shall be adjusted as necessary to exclude any emissions attributed to indirect land use change. Any such adjustment shall be based on regulations or methodologies determined by the Secretary in consultation with the Administrator of the Environmental Protection Agency and the Secretary of Agriculture. .\n##### (b) Conforming amendment\nSection 45Z(b)(1)(B)(i) of such Code is amended by striking clauses (ii) and (iii) and inserting clauses (ii), (iii), and (iv) .\n##### (c) Effective date\nThe amendments made by this section shall apply to emissions rates published for taxable years beginning after December 31, 2025.\n#### 4. Extension of clean fuel production credit\nSection 45Z(g) of the Internal Revenue Code of 1986 is amended by striking December 31, 2027 and inserting December 31, 2034 .\n#### 5. Rounding of clean fuel production credit emissions factor\n##### (a) In general\nSection 45Z(b)(2) of the Internal Revenue Code of 1986 is amended by striking 0.1 each place it appears and inserting 0.01 .\n##### (b) Effective date\nThe amendments made by this section shall apply to transportation fuel produced after December 31, 2024.",
      "versionDate": "2025-04-10",
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
        "actionDate": "2025-04-10",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1422",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Farmer First Fuel Incentives Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-05-28T13:59:09Z"
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
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2867ih.xml"
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
      "title": "Farmer First Fuel Incentives Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-25T08:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Farmer First Fuel Incentives Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-25T08:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to prohibit the use of foreign feedstocks for purposes of the clean fuel production credit, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-25T08:18:32Z"
    }
  ]
}
```
