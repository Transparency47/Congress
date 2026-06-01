# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4030?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4030
- Title: Treatment Continuity Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4030
- Origin chamber: House
- Introduced date: 2025-06-17
- Update date: 2025-10-07T08:05:36Z
- Update date including text: 2025-10-07T08:05:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-17: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-06-17: Introduced in House

## Actions

- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-17",
    "latestAction": {
      "actionDate": "2025-06-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4030",
    "number": "4030",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000628",
        "district": "2",
        "firstName": "Neal",
        "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
        "lastName": "Dunn",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Treatment Continuity Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-07T08:05:36Z",
    "updateDateIncludingText": "2025-10-07T08:05:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-17",
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
      "actionDate": "2025-06-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-17",
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
          "date": "2025-06-17T15:03:10Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "FL"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "FL"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4030ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4030\nIN THE HOUSE OF REPRESENTATIVES\nJune 17, 2025 Mr. Dunn of Florida (for himself, Mr. Soto , and Mr. Bean of Florida ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to authorize the Secretary of Health and Human Services to address priority substance use disorder and serious mental illness treatment needs through long-acting injectable medications, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Treatment Continuity Act of 2025 .\n#### 2. Priority substance use disorder and serious mental illness treatment needs of regional and national significance\n##### (a) In general\nSection 509 of the Public Health Service Act ( 42 U.S.C. 290bb\u20132 ) is amended\u2014\n**(1)**\nin the section heading, by inserting AND SERIOUS MENTAL ILLNESS after SUBSTANCE USE DISORDER ;\n**(2)**\nin subsection (a)\u2014\n**(A)**\nin the matter preceding paragraph (1), by inserting and serious mental illness after substance use disorder ; and\n**(B)**\nby striking paragraphs (1) through (3) and inserting the following:\n(1) access to long-acting injectable medications that are approved by the Food and Drug Administration for the treatment of individuals with substance use disorders or serious mental illness; (2) lab testing and supportive counseling for substance use disorder and serious mental illness; and (3) training on the use of long-acting injectable medications for the purposes described in paragraph (1), in combination with associated clinical services such as counseling. ;\n**(3)**\nin subsection (b)\u2014\n**(A)**\nin the subsection heading, by inserting and Serious Mental Illness after Substance Use Disorder ; and\n**(B)**\nin paragraphs (1) and (2), by inserting and serious mental illness after substance use disorder ;\n**(4)**\nby striking subsections (d) and (e) and inserting the following:\n(d) Annual report to Congress Not later than 1 year after the date of enactment of the Treatment Continuity Act of 2025, and annually thereafter during the term of the program under this section, the Secretary shall transmit to Congress a report on the outcomes of such program, including completed or substantial progress toward treatment requirements based on clinician assessment. ; and\n**(5)**\nby redesignating subsection (f) as subsection (e).\n##### (b) Applicability\nThe amendments made by this section shall apply to grants made under section 509 of the Public Health Service Act after the date of the enactment of this Act.",
      "versionDate": "2025-06-17",
      "versionType": "Introduced in House"
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
        "updateDate": "2025-07-09T12:43:24Z"
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
      "date": "2025-06-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4030ih.xml"
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
      "title": "Treatment Continuity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-27T11:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Treatment Continuity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-27T11:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to authorize the Secretary of Health and Human Services to address priority substance use disorder and serious mental illness treatment needs through long-acting injectable medications, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-27T11:18:22Z"
    }
  ]
}
```
