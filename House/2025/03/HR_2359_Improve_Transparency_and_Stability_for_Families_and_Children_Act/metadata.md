# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2359?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2359
- Title: Improve Transparency and Stability for Families and Children Act
- Congress: 119
- Bill type: HR
- Bill number: 2359
- Origin chamber: House
- Introduced date: 2025-03-26
- Update date: 2026-05-30T19:41:22Z
- Update date including text: 2026-05-30T19:41:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-26: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-26: Introduced in House

## Actions

- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Introduced in House
- 2025-03-26 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2359",
    "number": "2359",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "C001126",
        "district": "15",
        "firstName": "Mike",
        "fullName": "Rep. Carey, Mike [R-OH-15]",
        "lastName": "Carey",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Improve Transparency and Stability for Families and Children Act",
    "type": "HR",
    "updateDate": "2026-05-30T19:41:22Z",
    "updateDateIncludingText": "2026-05-30T19:41:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-26",
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
      "actionDate": "2025-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-26",
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
          "date": "2025-03-26T14:00:45Z",
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
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "OH"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2359ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2359\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2025 Mr. Carey (for himself and Mr. Miller of Ohio ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend part A of title IV of the Social Security Act to establish deadlines for the obligation and expenditure of funds and allow States to establish rainy day funds under the program of block grants to States for temporary assistance for needy families.\n#### 1. Short title\nThis Act may be cited as the Improve Transparency and Stability for Families and Children Act .\n#### 2. Deadlines for the obligation and expenditure of funds\n##### (a) In general\nSection 404(e) of the Social Security Act ( 42 U.S.C. 604(e) ) is amended to read as follows:\n(e) Deadlines for obligation and expenditure of funds by States (1) In general Except as provided in paragraph (2), a State to which funds are paid, after the effective date of this subsection, under section 403(a)(1) for a fiscal year shall obligate the funds not later than the end of the succeeding fiscal year, and shall expend the funds not later than the end of the 2nd succeeding fiscal year. (2) Exception for limited amount of funds set aside for future use (A) In general Notwithstanding paragraph (1) of this subsection, a State to which funds are paid under section 403(a)(1), after the effective date of this subsection, for a fiscal year may reserve not more than 15 percent of the funds for future use in the State program funded under this part, subject to subparagraph (B) of this paragraph. (B) Limitation The total amount held in reserve by a State under subparagraph (A) of this paragraph shall not exceed an amount equal to 50 percent of the total amount paid to the State under section 403(a)(1) for the then preceding fiscal year. (C) Notice of intent to reserve funds A State that intends to reserve funds under subparagraph (A) shall notify the Secretary of the intention not later than the end of the period in which the funds are available for obligation without regard to subparagraph (A) of this paragraph. .\n##### (b) Effective date\nThe amendment made by subsection (a) shall take effect on October 1, 2026.",
      "versionDate": "2025-03-26",
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
        "actionDate": "2026-05-29",
        "text": "Placed on the Union Calendar, Calendar No. 584."
      },
      "number": "8872",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Preventing Waste, Fraud, and Abuse in TANF Act",
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
        "name": "Social Welfare",
        "updateDate": "2025-04-04T15:56:31Z"
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
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2359ih.xml"
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
      "title": "Improve Transparency and Stability for Families and Children Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-04T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Improve Transparency and Stability for Families and Children Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend part A of title IV of the Social Security Act to establish deadlines for the obligation and expenditure of funds and allow States to establish rainy day funds under the program of block grants to States for temporary assistance for needy families.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T04:48:21Z"
    }
  ]
}
```
