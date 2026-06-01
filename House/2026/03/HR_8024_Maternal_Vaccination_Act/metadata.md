# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8024?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8024
- Title: Maternal Vaccination Act
- Congress: 119
- Bill type: HR
- Bill number: 8024
- Origin chamber: House
- Introduced date: 2026-03-19
- Update date: 2026-04-14T13:57:15Z
- Update date including text: 2026-04-14T13:57:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-19: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-03-19: Introduced in House

## Actions

- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-19",
    "latestAction": {
      "actionDate": "2026-03-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8024",
    "number": "8024",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001185",
        "district": "7",
        "firstName": "Terri",
        "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
        "lastName": "Sewell",
        "party": "D",
        "state": "AL"
      }
    ],
    "title": "Maternal Vaccination Act",
    "type": "HR",
    "updateDate": "2026-04-14T13:57:15Z",
    "updateDateIncludingText": "2026-04-14T13:57:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-19",
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
      "actionDate": "2026-03-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-19",
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
          "date": "2026-03-19T13:04:15Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8024ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8024\nIN THE HOUSE OF REPRESENTATIVES\nMarch 19, 2026 Ms. Sewell introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act with respect to maternal vaccination awareness and equity, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Maternal Vaccination Act .\n#### 2. Maternal vaccination awareness and equity campaign\n##### (a) Campaign\nSection 313 of the Public Health Service Act ( 42 U.S.C. 245 ) is amended\u2014\n**(1)**\nin subsection (a), by inserting and among pregnant and postpartum individuals, after low rates of vaccination, ;\n**(2)**\nin subsection (c)(3), by striking prenatal and pediatric and inserting prenatal, obstetric, and pediatric ;\n**(3)**\nin subsection (d)(4)(B), by inserting pregnant and postpartum individuals and after including ; and\n**(4)**\nin subsection (g), by striking $15,000,000 for each of fiscal years 2021 through 2025 and inserting $17,000,000 for each of fiscal years 2027 through 2031 .\n##### (b) Additional activities\nSection 317(k)(1)(E) of the Public Health Service Act ( 42 U.S.C. 247b(k)(1)(E) ) is amended\u2014\n**(1)**\nin clause (v), by striking and at the end; and\n**(2)**\nby adding at the end the following:\n(vii) increase vaccination rates of pregnant and postpartum individuals, including individuals from racial and ethnic minority groups, and their children; and .",
      "versionDate": "2026-03-19",
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
        "actionDate": "2026-03-18",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "4132",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Maternal Vaccinations Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-03-18",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Education and Workforce, Veterans' Affairs, Natural Resources, and the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "7973",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Momnibus Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-03-27",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "8153",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Maternal Vaccination Act",
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
        "name": "Health",
        "updateDate": "2026-04-03T20:28:42Z"
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
      "date": "2026-03-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8024ih.xml"
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
      "title": "Maternal Vaccination Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-02T12:08:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Maternal Vaccination Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-02T12:08:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act with respect to maternal vaccination awareness and equity, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-02T12:03:27Z"
    }
  ]
}
```
