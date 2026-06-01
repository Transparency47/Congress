# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/617?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/617
- Title: OPIOIDS Act
- Congress: 119
- Bill type: S
- Bill number: 617
- Origin chamber: Senate
- Introduced date: 2025-02-18
- Update date: 2026-04-06T16:15:37Z
- Update date including text: 2026-04-06T16:15:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-18: Introduced in Senate
- 2025-02-18 - IntroReferral: Introduced in Senate
- 2025-02-18 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-02-18: Introduced in Senate

## Actions

- 2025-02-18 - IntroReferral: Introduced in Senate
- 2025-02-18 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-18",
    "latestAction": {
      "actionDate": "2025-02-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/617",
    "number": "617",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "OPIOIDS Act",
    "type": "S",
    "updateDate": "2026-04-06T16:15:37Z",
    "updateDateIncludingText": "2026-04-06T16:15:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-18",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-18",
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
          "date": "2025-02-18T22:55:44Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "VT"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s617is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 617\nIN THE SENATE OF THE UNITED STATES\nFebruary 18, 2025 Mr. Scott of Florida (for himself and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo permit the Attorney General to award grants for accurate data on opioid-related overdoses, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Overcoming Prevalent Inadequacies in Overdose Information Data Sets Act or the OPIOIDS Act .\n#### 2. Accurate data on opioid-related overdoses\nThe Attorney General may award grants to States, territories, and localities to support improved data and surveillance on opioid-related overdoses, including for activities to improve postmortem toxicology testing, data linkage across data systems throughout the United States, electronic death reporting, or the comprehensiveness of data on fatal and nonfatal opioid-related overdoses.\n#### 3. Law enforcement grants\n##### (a) In general\nThe Attorney General shall make grants to local law enforcement agencies and forensic laboratories in communities with high rates of drug overdoses for the purpose of\u2014\n**(1)**\ntraining to help officers identify overdoses;\n**(2)**\nupgrading essential systems for tracing drugs and processing samples in forensic laboratories to provide timely, accurate, and standard data reporting to the National Forensic Laboratory Information System; or\n**(3)**\ntraining to better trace criminals through the darknet.\n##### (b) Mandatory reporting\nNone of the funds made under subsection (a) may be used by grantees that do not submit to the National Forensic Laboratory Information System reports on overdose data.\n##### (c) Federal Law Enforcement Training Centers\nFederal Law Enforcement Training Centers shall provide training to State and local law enforcement agencies on how to best coordinate with State and Federal partners for tracking drug-related activity.\n##### (d) COPS grants\nSection 1701(b) of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10381 ) is amended\u2014\n**(1)**\nin paragraph (23), by striking and at the end;\n**(2)**\nin paragraph (24), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(24) to provide training and resources for containment devices to prevent secondary exposure to fentanyl and other substances for first responders. .\n#### 4. Office of National Drug Control Policy reform\n##### (a) In general\nThe Drug Enforcement Administration shall develop uniform reporting standards for inputting data into the National Forensic Laboratory Information System for purity, formulation, and weight to allow for better comparison across jurisdictions and between agencies and the sharing of data.\n##### (b) Clarification\nNothing in subsection (a) may be construed to require the creation of new or increased obligations or reporting requirements on State or local laboratories.\n#### 5. DEA testing\nThe Drug Enforcement Administration shall submit to Congress, as part of the annual budget process, a specific line item for the level of funding necessary for the Fentanyl Signature Profiling Program.",
      "versionDate": "2025-02-18",
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
        "actionDate": "2025-02-12",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "1257",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "OPIOIDS Act",
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
            "name": "Computers and information technology",
            "updateDate": "2025-05-02T15:11:02Z"
          },
          {
            "name": "Drug, alcohol, tobacco use",
            "updateDate": "2025-05-02T15:11:02Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-05-02T15:11:02Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-05-02T15:11:02Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2025-05-02T15:11:02Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-05-02T15:11:02Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-13T15:04:52Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-18",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s617",
          "measure-number": "617",
          "measure-type": "s",
          "orig-publish-date": "2025-02-18",
          "originChamber": "SENATE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s617v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2025-02-18",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><b>Overcoming Prevalent Inadequacies in Overdose Information Data Sets Act or the OPIOIDS Act </b></p> <p>This bill establishes and revises certain grants and resources to address opioid-related overdoses.</p> <p>Specifically, the bill authorizes the Department of Justice (DOJ) to award grants to states, territories, and localities to improve data and surveillance related to opioid overdoses.</p> <p>Additionally, the bill directs DOJ to award grants to law enforcement agencies and forensic laboratories in communities with high rates of drug overdoses to (1) provide training to help officers better identify overdoses, (2) upgrade essential systems for drug tracing and processing samples in forensic laboratories, or (3) provide training to better trace criminals through the dark web.</p> <p>The bill requires the Federal Law Enforcement Training Centers to provide training to state and local law enforcement agencies on how to best coordinate with state and federal partners for tracking drug-related activity.</p> <p>The bill allows funds under the Community Oriented Policing Services grant program to be used to provide training and resources for equipment that protects first responders from secondary fentanyl exposure.</p> <p>Finally, the bill directs the Drug Enforcement Administration to (1) develop uniform reporting standards for information concerning drug control activities, and (2) budget for a program that analyzes fentanyl samples.</p>"
        },
        "title": "OPIOIDS Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s617.xml",
    "summary": {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Overcoming Prevalent Inadequacies in Overdose Information Data Sets Act or the OPIOIDS Act </b></p> <p>This bill establishes and revises certain grants and resources to address opioid-related overdoses.</p> <p>Specifically, the bill authorizes the Department of Justice (DOJ) to award grants to states, territories, and localities to improve data and surveillance related to opioid overdoses.</p> <p>Additionally, the bill directs DOJ to award grants to law enforcement agencies and forensic laboratories in communities with high rates of drug overdoses to (1) provide training to help officers better identify overdoses, (2) upgrade essential systems for drug tracing and processing samples in forensic laboratories, or (3) provide training to better trace criminals through the dark web.</p> <p>The bill requires the Federal Law Enforcement Training Centers to provide training to state and local law enforcement agencies on how to best coordinate with state and federal partners for tracking drug-related activity.</p> <p>The bill allows funds under the Community Oriented Policing Services grant program to be used to provide training and resources for equipment that protects first responders from secondary fentanyl exposure.</p> <p>Finally, the bill directs the Drug Enforcement Administration to (1) develop uniform reporting standards for information concerning drug control activities, and (2) budget for a program that analyzes fentanyl samples.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119s617"
    },
    "title": "OPIOIDS Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Overcoming Prevalent Inadequacies in Overdose Information Data Sets Act or the OPIOIDS Act </b></p> <p>This bill establishes and revises certain grants and resources to address opioid-related overdoses.</p> <p>Specifically, the bill authorizes the Department of Justice (DOJ) to award grants to states, territories, and localities to improve data and surveillance related to opioid overdoses.</p> <p>Additionally, the bill directs DOJ to award grants to law enforcement agencies and forensic laboratories in communities with high rates of drug overdoses to (1) provide training to help officers better identify overdoses, (2) upgrade essential systems for drug tracing and processing samples in forensic laboratories, or (3) provide training to better trace criminals through the dark web.</p> <p>The bill requires the Federal Law Enforcement Training Centers to provide training to state and local law enforcement agencies on how to best coordinate with state and federal partners for tracking drug-related activity.</p> <p>The bill allows funds under the Community Oriented Policing Services grant program to be used to provide training and resources for equipment that protects first responders from secondary fentanyl exposure.</p> <p>Finally, the bill directs the Drug Enforcement Administration to (1) develop uniform reporting standards for information concerning drug control activities, and (2) budget for a program that analyzes fentanyl samples.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119s617"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s617is.xml"
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
      "title": "OPIOIDS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-21T12:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "OPIOIDS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Overcoming Prevalent Inadequacies in Overdose Information Data Sets Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to permit the Attorney General to award grants for accurate data on opioid-related overdoses, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:03:35Z"
    }
  ]
}
```
