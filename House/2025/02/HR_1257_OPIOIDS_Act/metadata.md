# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1257?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1257
- Title: OPIOIDS Act
- Congress: 119
- Bill type: HR
- Bill number: 1257
- Origin chamber: House
- Introduced date: 2025-02-12
- Update date: 2025-12-06T06:52:23Z
- Update date including text: 2025-12-06T06:52:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-12: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-02-12: Introduced in House

## Actions

- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Introduced in House
- 2025-02-12 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1257",
    "number": "1257",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "L000597",
        "district": "15",
        "firstName": "Laurel",
        "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
        "lastName": "Lee",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "OPIOIDS Act",
    "type": "HR",
    "updateDate": "2025-12-06T06:52:23Z",
    "updateDateIncludingText": "2025-12-06T06:52:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-12",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-12",
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
          "date": "2025-02-12T15:02:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "NH"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1257ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1257\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2025 Ms. Lee of Florida (for herself and Mr. Pappas ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo permit the Attorney General to award grants for accurate data on opioid-related overdoses, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Overcoming Prevalent Inadequacies in Overdose Information Data Sets Act or the OPIOIDS Act .\n#### 2. Accurate data on opioid-related overdoses\nThe Attorney General may award grants to States, territories, and localities to support improved data and surveillance on opioid-related overdoses, including for activities to improve postmortem toxicology testing, data linkage across data systems throughout the United States, training to equip officers to address overdoses and related criminal activity, electronic death reporting, or the comprehensiveness of data on fatal opioid-related overdoses.\n#### 3. Law enforcement grants\n##### (a) In general\nThe Attorney General may make grants to local law enforcement agencies and forensic laboratories in communities with high rates of drug overdoses for the purpose of\u2014\n**(1)**\ntraining to help officers identify overdoses;\n**(2)**\nupgrading essential systems for tracing drugs and processing samples in forensic laboratories to provide timely, accurate, and standard data reporting to the National Forensic Laboratory Information System;\n**(3)**\ntraining to better trace criminals through the darknet; or\n**(4)**\nproviding training, staffing, and equipment in medical examiners and coroners\u2019 offices to provide more timely and comprehensive services in suspected overdose cases.\n##### (b) Mandatory reporting\nNone of the funds made under subsection (a) may be used by grantees that do not submit to the National Forensic Laboratory Information System reports on overdose data.\n##### (c) Federal Law Enforcement Training Centers\nFederal Law Enforcement Training Centers shall provide training to State and local law enforcement agencies on how to best coordinate with State and Federal partners for tracking drug-related activity.\n##### (d) COPS grants\nSection 1701(b) of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10381 ) is amended\u2014\n**(1)**\nin paragraph (23), by striking and at the end;\n**(2)**\nin paragraph (24), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(25) to provide training and resources for containment devices to prevent secondary exposure to fentanyl and other substances for first responders. .\n#### 4. Office of National Drug Control Policy reform\n##### (a) In general\nThe Drug Enforcement Administration shall develop uniform reporting standards for inputting data into the National Forensic Laboratory Information System for purity, formulation, and weight to allow for better comparison across jurisdictions and between agencies and the sharing of data.\n##### (b) Clarification\nNothing in subsection (a) may be construed to require the creation of new or increased obligations or reporting requirements on State or local laboratories.\n#### 5. DEA testing\nThe Drug Enforcement Administration shall submit to Congress, as part of the annual budget process, a specific line item for the level of funding necessary for the Fentanyl Signature Profiling Program.",
      "versionDate": "2025-02-12",
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
        "actionDate": "2025-02-18",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "617",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "OPIOIDS Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Computers and information technology",
            "updateDate": "2025-05-02T15:10:41Z"
          },
          {
            "name": "Drug, alcohol, tobacco use",
            "updateDate": "2025-05-02T15:10:14Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-05-02T15:10:33Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-05-02T15:10:27Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2025-05-02T15:10:21Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-05-02T15:10:48Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-17T15:56:34Z"
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
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1257ih.xml"
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
      "title": "OPIOIDS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-14T09:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "OPIOIDS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-14T09:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Overcoming Prevalent Inadequacies in Overdose Information Data Sets Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-14T09:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To permit the Attorney General to award grants for accurate data on opioid-related overdoses, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-14T09:18:24Z"
    }
  ]
}
```
