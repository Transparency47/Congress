# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4130?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4130
- Title: COST Act
- Congress: 119
- Bill type: S
- Bill number: 4130
- Origin chamber: Senate
- Introduced date: 2026-03-18
- Update date: 2026-05-01T18:40:49Z
- Update date including text: 2026-05-01T18:40:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-18: Introduced in Senate
- 2026-03-18 - Committee: Committee on Small Business and Entrepreneurship. Hearings held.
- 2026-03-18 - IntroReferral: Introduced in Senate
- 2026-03-18 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2026-03-18: Introduced in Senate

## Actions

- 2026-03-18 - Committee: Committee on Small Business and Entrepreneurship. Hearings held.
- 2026-03-18 - IntroReferral: Introduced in Senate
- 2026-03-18 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4130",
    "number": "4130",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "E000295",
        "district": "",
        "firstName": "Joni",
        "fullName": "Sen. Ernst, Joni [R-IA]",
        "lastName": "Ernst",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "COST Act",
    "type": "S",
    "updateDate": "2026-05-01T18:40:49Z",
    "updateDateIncludingText": "2026-05-01T18:40:49Z"
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
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Small Business and Entrepreneurship. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
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
          "date": "2026-03-18T18:30:08Z",
          "name": "Hearings By (full committee)"
        }
      },
      "chamber": "Senate",
      "name": "Small Business and Entrepreneurship Committee",
      "systemCode": "sssb00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-03-18T17:09:16Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "FL"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "WY"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4130is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4130\nIN THE SENATE OF THE UNITED STATES\nMarch 18, 2026 Ms. Ernst (for herself and Mr. Scott of Florida ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo put a public price tag on all projects supported with taxpayer dollars.\n#### 1. Short title\nThis Act may be cited as the Cost Openness and Spending Transparency Act of 2026 or the COST Act .\n#### 2. Disclosure requirements for Federal funds\n##### (a) In general\nSubchapter III of chapter 13 of title 31, United States Code, is amended by adding at the end the following:\n1356. Disclosure requirements for Federal funds (a) Definition In this section, the term agency means\u2014 (1) an Executive agency, as defined in section 105 of title 5; and (2) an independent regulatory agency, as defined in section 3502 of title 44. (b) Disclosure requirements An agency and an individual or entity (including a State or local government and a recipient of a Federal research grant) carrying out a program, project, or activity that is, in whole or in part, carried out using Federal funds shall clearly state in any statement, press release, request for proposals, bid solicitation, or other document describing the program, project, or activity, other than a communication containing not more than 280 characters\u2014 (1) the percentage of the total costs of the program, project, or activity which will be financed with Federal funds; (2) the dollar amount of the Federal funds made available for the program, project, or activity; and (3) the percentage of the total costs of, and dollar amount for, the program, project, or activity that will be financed by nongovernmental sources. (c) Certification An individual or entity carrying out a program, project, or activity that is, in whole or in part, carried out using Federal funds shall, as part of the performance progress reporting regarding the program, project, or activity, include a certification indicating whether the individual or entity complied with the disclosure requirements under subsection (b) with respect to communications containing not more than 280 characters relating to the program, project, or activity. (d) Compliance review The Director of the Office of Management and Budget shall annually\u2014 (1) review a random sampling of public communications issued by agencies and recipients of Federal funds for compliance with the disclosure requirements under subsection (b); and (2) make publicly available the findings of the review under paragraph (1). (e) Public reporting Not later than 1 year after the date of enactment of this section, the Director of the Office of Management and Budget shall make available to the public a mechanism to anonymously report communications that do not comply with the disclosure requirements under subsection (b), which shall require that such a report include\u2014 (1) the noncompliant communication or, if publicly available, the location of the noncompliant communication; and (2) identifying information regarding the program, project, or activity that is, in whole or in part, carried out using Federal funds. .\n##### (b) Technical and conforming amendment\nThe table of sections for subchapter III of chapter 13 of title 31, United States Code, is amended by adding at the end the following:\n1356. Disclosure requirements for Federal funds. .",
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
        "actionDate": "2025-02-14",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "1387",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "COST Act",
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
        "item": {
          "name": "Government information and archives",
          "updateDate": "2026-05-01T18:40:49Z"
        }
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2026-03-30T23:08:14Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4130is.xml"
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
      "title": "COST Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-14T11:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "COST Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T04:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Cost Openness and Spending Transparency Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T04:23:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to put a public price tag on all projects supported with taxpayer dollars.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-25T04:18:39Z"
    }
  ]
}
```
