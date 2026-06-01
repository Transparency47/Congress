# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/786?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/786
- Title: Public Health Funding Restoration Act
- Congress: 119
- Bill type: S
- Bill number: 786
- Origin chamber: Senate
- Introduced date: 2025-02-27
- Update date: 2025-12-05T21:51:29Z
- Update date including text: 2025-12-05T21:51:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-27: Introduced in Senate
- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-02-27: Introduced in Senate

## Actions

- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/786",
    "number": "786",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Public Health Funding Restoration Act",
    "type": "S",
    "updateDate": "2025-12-05T21:51:29Z",
    "updateDateIncludingText": "2025-12-05T21:51:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-27",
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
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T18:18:59Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "MN"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "MN"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "WA"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "OR"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "MA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s786is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 786\nIN THE SENATE OF THE UNITED STATES\nFebruary 27, 2025 Mr. Blumenthal (for himself, Ms. Smith , Ms. Klobuchar , Mrs. Murray , Mr. Wyden , Mr. Markey , and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo fully fund the Prevention and Public Health Fund and reaffirm the importance of prevention in the United States healthcare system.\n#### 1. Short title\nThis Act may be cited as the Public Health Funding Restoration Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe Prevention and Public Health Fund (section 4002 of the Patient Protection and Affordable Care Act ( 42 U.S.C. 300u\u201311 ) was designed to provide for expanded and sustained national investment in prevention and public health programs to improve health and help restrain the rate of growth in private and public health care costs .\n**(2)**\nFunding under such section is essential to core efforts at the Department of Health and Human Services and in State, local, Tribal, and territorial health departments to prevent and control the spread of infectious disease and prevent injuries and the development of chronic conditions.\n**(3)**\nPrevention and Public Health Fund dollars support evidenced-based investments in tobacco use prevention and cessation, nutrition, mental health, childhood lead poisoning prevention, elder care initiatives, and immunizations, among other prevention initiatives. Funding gives States and communities the flexibility to respond to public health threats that may be unique to their communities and bolsters the State, local, Tribal, and territorial response to global public health threats.\n**(4)**\nSuch prevention efforts have shown to be effective. Funding increases for community-based public health programs reduce infant deaths and preventable deaths caused by cancer, diabetes, and cardiovascular disease. Every dollar spent on prevention saves nearly $6 in health spending and every dollar spent on childhood vaccines saves $16.50 in future health care costs.\n**(5)**\nInvestments in prevention reduce the cost of health care in the United States. $2,900,000,000 in investments in community-based disease prevention is estimated to save $16,500,000,000 annually within 5 years.\n**(6)**\nCuts to the Prevention and Public Health Fund and other public health prevention efforts undermine efforts to create an affordable and accessible health care system, and a better quality of life for Americans.\n**(7)**\nCuts to the Prevention and Public Health Fund endanger the ability of States and localities to distribute vaccinations and public health information successfully. The Prevention and Public Health Fund is critical to the growth of the Centers for Disease Control and Prevention\u2019s section 317 Immunization Program and to the Epidemiology and Laboratory Capacity program.\n**(8)**\nRestoring Prevention and Public Health Fund funding to $2,000,000,000 annually will allow the Fund to invest in more innovative, evidence-based public health programs and maintain and expand investments in programs with demonstrated success.\n**(9)**\nRestoring Prevention and Public Health Fund funding to $2,000,000,000 will give the Centers for Disease Control and Prevention and State, local, Tribal, and territorial health departments funding that they need to invest in prevention efforts that will help the country avoid future pandemics and epidemics.\n#### 3. Prevention and public health fund\nSection 4002(b) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 300u\u201311(b) ) is amended\u2014\n**(1)**\nin paragraph (4), by adding at the end and ; and\n**(2)**\nby striking paragraphs (5) through (10) and inserting the following:\n(5) for fiscal year 2026 and each fiscal year thereafter, $2,000,000,000. .",
      "versionDate": "2025-02-27",
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
        "actionDate": "2025-02-27",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "1715",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Public Health Funding Restoration Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Appropriations",
            "updateDate": "2025-09-02T19:06:11Z"
          },
          {
            "name": "Government trust funds",
            "updateDate": "2025-09-02T19:06:11Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-09-02T19:06:11Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-09-02T19:06:11Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-21T17:30:54Z"
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
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s786is.xml"
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
      "title": "Public Health Funding Restoration Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Public Health Funding Restoration Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to fully fund the Prevention and Public Health Fund and reaffirm the importance of prevention in the United States healthcare system.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:04:08Z"
    }
  ]
}
```
