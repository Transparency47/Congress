# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4132?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4132
- Title: Maternal Vaccinations Act
- Congress: 119
- Bill type: S
- Bill number: 4132
- Origin chamber: Senate
- Introduced date: 2026-03-18
- Update date: 2026-04-14T13:57:13Z
- Update date including text: 2026-04-14T13:57:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-18: Introduced in Senate
- 2026-03-18 - IntroReferral: Introduced in Senate
- 2026-03-18 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-03-18: Introduced in Senate

## Actions

- 2026-03-18 - IntroReferral: Introduced in Senate
- 2026-03-18 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-18",
    "latestAction": {
      "actionDate": "2026-03-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4132",
    "number": "4132",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000384",
        "district": "",
        "firstName": "Timothy",
        "fullName": "Sen. Kaine, Tim [D-VA]",
        "lastName": "Kaine",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Maternal Vaccinations Act",
    "type": "S",
    "updateDate": "2026-04-14T13:57:13Z",
    "updateDateIncludingText": "2026-04-14T13:57:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-18",
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
          "date": "2026-03-18T17:12:26Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4132is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4132\nIN THE SENATE OF THE UNITED STATES\nMarch 18, 2026 Mr. Kaine introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Public Health Service Act to increase vaccination rates of pregnant and postpartum individuals, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Maternal Vaccinations Act .\n#### 2. Maternal vaccination awareness and equity campaign\n##### (a) Campaign\nSection 313 of the Public Health Service Act ( 42 U.S.C. 245 ) is amended\u2014\n**(1)**\nin subsection (a), by inserting and among pregnant and postpartum individuals, after low rates of vaccination, ;\n**(2)**\nin subsection (c)(3), by striking prenatal and pediatric and inserting prenatal, obstetric, and pediatric ;\n**(3)**\nin subsection (d)(4)(B), by inserting pregnant and postpartum individuals and after including ; and\n**(4)**\nin subsection (g), by striking $15,000,000 for each of fiscal years 2021 through 2025 and inserting $17,000,000 for each of fiscal years 2027 through 2031 .\n##### (b) Additional activities\nSection 317(k)(1)(E) of the Public Health Service Act ( 42 U.S.C. 247b(k)(1)(E) ) is amended\u2014\n**(1)**\nin clause (v), by striking and at the end; and\n**(2)**\nby adding at the end the following:\n(vii) increase vaccination rates of pregnant and postpartum individuals, including individuals from racial and ethnic minority groups, and their children; and .",
      "versionDate": "2026-03-18",
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
        "actionDate": "2026-03-19",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "8024",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Maternal Vaccination Act",
      "type": "HR"
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
          "type": "Related bill"
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
        "updateDate": "2026-04-01T13:49:37Z"
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
      "date": "2026-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4132is.xml"
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
      "title": "Maternal Vaccinations Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-25T04:23:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Maternal Vaccinations Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T04:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Public Health Service Act to increase vaccination rates of pregnant and postpartum individuals, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-25T04:18:38Z"
    }
  ]
}
```
