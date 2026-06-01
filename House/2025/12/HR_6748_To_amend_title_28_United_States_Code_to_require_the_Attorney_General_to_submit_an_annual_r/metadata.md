# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6748?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6748
- Title: Gang Activity Reporting Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6748
- Origin chamber: House
- Introduced date: 2025-12-16
- Update date: 2026-01-09T16:23:35Z
- Update date including text: 2026-01-09T16:23:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-16: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-12-16: Introduced in House

## Actions

- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-16",
    "latestAction": {
      "actionDate": "2025-12-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6748",
    "number": "6748",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "H001091",
        "district": "2",
        "firstName": "Ashley",
        "fullName": "Rep. Hinson, Ashley [R-IA-2]",
        "lastName": "Hinson",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Gang Activity Reporting Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-09T16:23:35Z",
    "updateDateIncludingText": "2026-01-09T16:23:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-16",
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
      "actionDate": "2025-12-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-16",
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
          "date": "2025-12-16T15:00:40Z",
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
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6748ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6748\nIN THE HOUSE OF REPRESENTATIVES\nDecember 16, 2025 Mrs. Hinson (for herself and Ms. Kaptur ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 28, United States Code, to require the Attorney General to submit an annual report to Congress on gang activity, reporting, investigation, and prosecution, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Gang Activity Reporting Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe United States is experiencing an unprecedented surge in violent crime, including an increase of more than 30 percent in the rate of murders since 2020.\n**(2)**\nThe most recent Department of Justice data regarding gangs and criminal activity, published in the 2011 National Gang Threat Assessment, indicated that gangs were responsible for an average of 48 percent of violent crime in the United States.\n**(3)**\nUp-to-date, accurate, and consistent reporting from the relevant Federal agencies relating to gang activity in the United States is a foundational element in enabling policymakers to enact effective, evidence-based policy that protects the people of the United States from gang activity.\n#### 3. Gang reporting requirement\n##### (a) In general\nChapter 31 of title 28, United States Code, is amended by adding at the end the following:\n530E. Report on gang activity, reporting, investigation, and prosecution (a) Report (1) In general Not later than 150 days after the date of enactment of the Gang Activity Reporting Act of 2025 , and not later than the last day of each fiscal year beginning after the date of enactment, the Attorney General shall, in conjunction with the Secretary of Homeland Security and the Director of the Federal Bureau of Investigation, and in coordination with State and local law enforcement agencies, submit to the Committee on the Judiciary and the Committee on Appropriations of the Senate and the Committee on the Judiciary and the Committee on Appropriations of the House of Representatives a report on gang activity, reporting, investigation, and prosecution. (2) Contents The report described in paragraph (1) shall include information relating to\u2014 (A) the growth of local, national, and transnational gangs during the 10-fiscal-year period preceding the date on which the report is submitted (referred to in this section as the submission date )\u2014 (i) with specific numerical data; (ii) including changes and trends in gang membership, location, and activities and enterprises; and (iii) including relevant data from State and local law enforcement agencies; (B) the tools, methods, or networks that gangs are using to commit certain crimes, including\u2014 (i) the extent to which gangs cooperate; and (ii) an assessment of the kinds of crimes on which gangs cooperate; (C) whether and to what extent State-based reporting issues affect Federal data collection and accuracy; (D) the initiatives the Department of Justice, Department of Homeland Security, and Federal Bureau of Investigation undertook during the 5-fiscal-year period preceding the submission date to track gang growth and gang activity and to investigate and prosecute related unlawful activity, including\u2014 (i) the date on which each initiative was undertaken; and (ii) if applicable, the date on which each initiative was ended, with a detailed explanation as to why the initiative was ended; (E) the Federal resources allocated by each agency described in subparagraph (D) to investigating, prosecuting, and containing gangs as of the submission date; (F) gang enforcement statistics from the last fiscal year ending before the submission date, including the quantity, changes, and trends in\u2014 (i) gang-related arrests, including comparisons to gang-related arrests during the 5-fiscal-year period preceding the applicable fiscal year; (ii) the number of juveniles arrested as a result of gang-related activity; (iii) the number of firearms seized by law enforcement agencies during gang enforcement operations, including the number of firearms seized from juveniles; and (iv) the amount in weight of fentanyl, methamphetamine, and other synthetic opioids seized by law enforcement agencies during gang enforcement operations, including the amount of fentanyl, methamphetamine, and other synthetic opioids seized from juveniles; (G) the data collection procedures utilized by each agency described in subparagraph (D); and (H) any changes to data collection procedures of an agency described in subparagraph (D) during the 18-month period preceding the submission date, including explanations as to why any procedures were changed. (b) Classification The report submitted under subsection (a), or a portion thereof, may be classified, as determined appropriate by the Attorney General, the Secretary of Homeland Security, and the Director of the Federal Bureau of Investigation. .\n##### (b) Technical amendment\nThe table of sections for chapter 31 of title 28, United States Code, is amended by adding at the end the following:\n530E. Report on gang activity, reporting, investigation, and prosecution. .",
      "versionDate": "2025-12-16",
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
        "actionDate": "2025-10-23",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "3046",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Gang Activity Reporting Act of 2025",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-01-09T16:23:35Z"
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
      "date": "2025-12-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6748ih.xml"
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
      "title": "Gang Activity Reporting Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-08T11:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Gang Activity Reporting Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-08T11:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 28, United States Code, to require the Attorney General to submit an annual report to Congress on gang activity, reporting, investigation, and prosecution, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-08T11:18:21Z"
    }
  ]
}
```
