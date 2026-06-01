# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1279?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1279
- Title: To amend title XIX of the Social Security Act to establish a community engagement requirement for certain individuals under the Medicaid program.
- Congress: 119
- Bill type: HR
- Bill number: 1279
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2025-07-07T15:03:40Z
- Update date including text: 2025-07-07T15:03:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-13: Introduced in House

## Actions

- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1279",
    "number": "1279",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001314",
        "district": "4",
        "firstName": "Aaron",
        "fullName": "Rep. Bean, Aaron [R-FL-4]",
        "lastName": "Bean",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "To amend title XIX of the Social Security Act to establish a community engagement requirement for certain individuals under the Medicaid program.",
    "type": "HR",
    "updateDate": "2025-07-07T15:03:40Z",
    "updateDateIncludingText": "2025-07-07T15:03:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
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
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T14:03:15Z",
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
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "TX"
    },
    {
      "bioguideId": "K000403",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Kennedy, Mike [R-UT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "UT"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "FL"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1279ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1279\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Mr. Bean of Florida (for himself, Mr. Weber of Texas , Mr. Kennedy of Utah , and Mr. Scott Franklin of Florida ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XIX of the Social Security Act to establish a community engagement requirement for certain individuals under the Medicaid program.\n#### 1. Community engagement requirement for applicable individuals\n##### (a) In general\nSection 1903(i) of the Social Security Act ( 42 U.S.C. 1396b(i) ) is amended\u2014\n**(1)**\nin paragraph (26), by striking ; or and inserting a semicolon;\n**(2)**\nin paragraph (27), by striking the period at the end and inserting ; or ;\n**(3)**\nby inserting after paragraph (27) the following new paragraph:\n(28) with respect to any amount expended for medical assistance for an applicable individual for a month in a calendar year if such individual did not meet the community engagement requirement under section 1905(kk) for 3 or more preceding months during such calendar year while such individual was an applicable individual and was enrolled in a State plan (or waiver of such plan) under this title. ; and\n**(4)**\nin the flush left matter at the end, by striking and (18), and inserting (18), and (28) .\n##### (b) Community engagement requirement\nSection 1905 of the Social Security Act ( 42 U.S.C. 1396d ) is amended by adding at the end the following new subsection:\n(kk) Community engagement requirement for applicable individuals (1) Community engagement requirement described For purposes of section 1903(i)(28), the community engagement requirement described in this subsection with respect to an applicable individual and a month is that such individual satisfies at least one of the following with respect to such month: (A) The individual works 80 hours or more per month, or has a monthly income that is at least equal to the Federal minimum wage under section 6 of the Fair Labor Standards Act of 1938, multiplied by 80 hours. (B) The individual completes 80 hours or more of community service per month. (C) The individual participates in a work program for at least 80 hours per month. (D) The individual participates in a combination of work, including community service, and a work program for a total of at least 80 hours per month. (2) Verification For purposes of verifying the compliance of an applicable individual with the community engagement requirement under paragraph (1), a State Medicaid agency shall, whenever possible, prioritize the utilization of existing databases or other verification measures, including the National Change of Address Database Maintained by the United States Postal Service, State health and human services agencies, payroll databases, or other reliable sources of information, prior to seeking additional verification from such individual. (3) Definitions In this subsection: (A) Applicable individual The term applicable individual means any individual who is not\u2014 (i) under 18 years of age or over 65 years of age; (ii) physically or mentally unfit for employment, as determined by a physician or other medical professional; (iii) pregnant; (iv) the parent or caretaker of a dependent child; (v) the parent or caretaker of an incapacitated person; (vi) complying with work requirements under a different program under Federal law; (vii) participating in a drug or alcohol treatment and rehabilitation program (as defined in section 3(h) of the Food and Nutrition Act of 2008); or (viii) enrolled in an educational program at least half time. (B) Educational program The term educational program means\u2014 (i) an institution of higher education (as defined in section 101(a) of the Higher Education Act of 1965); (ii) a program of career and technical education (as defined in section 3 of the Carl D. Perkins Career and Technical Education Act of 2006); or (iii) any other educational program approved by the Secretary. (C) State medicaid agency The term State Medicaid agency means the State agency responsible for administering the State Medicaid plan. (D) Work program The term work program has the meaning given such term in section 6(o)(1) of the Food and Nutrition Act of 2008. .\n##### (c) State option To disenroll certain individuals\nSection 1902(a) of the Social Security Act ( 42 U.S.C. 1396a(a) ) is amended by adding at the end of the flush left text following paragraph (87) the following: Notwithstanding any of the preceding provisions of this subsection, at the option of a State, such State may elect to disenroll an applicable individual for a month if, with respect to medical assistance furnished to such individual for such month, no Federal financial participation would be available, pursuant to section 1903(i)(28). .",
      "versionDate": "2025-02-13",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Employment and training programs",
            "updateDate": "2025-07-07T15:03:22Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-07-07T15:03:40Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-07-07T15:03:09Z"
          },
          {
            "name": "Medicaid",
            "updateDate": "2025-07-07T15:03:01Z"
          },
          {
            "name": "National and community service",
            "updateDate": "2025-07-07T15:03:15Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-07-07T15:03:32Z"
          },
          {
            "name": "Temporary and part-time employment",
            "updateDate": "2025-07-07T15:03:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-17T15:46:18Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
    "originChamber": "House",
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
          "measure-id": "id119hr1279",
          "measure-number": "1279",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-13",
          "originChamber": "HOUSE",
          "update-date": "2025-06-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1279v00",
            "update-date": "2025-06-13"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill establishes community engagement requirements (i.e., work requirements) for certain adults under Medicaid.</p><p>Specifically, the bill requires individuals ages 18 through 65 to work, engage in community service, or participate in a work program (or a combination of these) for at least 80 hours per month. The bill prohibits federal payments for, and allows state Medicaid programs to disenroll, individuals who do not meet these requirements for three or more months in a year.</p><p>The requirements do not apply to individuals who are (1) physically or mentally unfit to work, (2) pregnant, (3) parents or caretakers of children or incapacitated individuals, (4) complying with work requirements for other federal programs, (5) participating in a drug or alcohol treatment and rehabilitation program, or (6) enrolled at least half-time in school.</p>"
        },
        "title": "To amend title XIX of the Social Security Act to establish a community engagement requirement for certain individuals under the Medicaid program."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1279.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill establishes community engagement requirements (i.e., work requirements) for certain adults under Medicaid.</p><p>Specifically, the bill requires individuals ages 18 through 65 to work, engage in community service, or participate in a work program (or a combination of these) for at least 80 hours per month. The bill prohibits federal payments for, and allows state Medicaid programs to disenroll, individuals who do not meet these requirements for three or more months in a year.</p><p>The requirements do not apply to individuals who are (1) physically or mentally unfit to work, (2) pregnant, (3) parents or caretakers of children or incapacitated individuals, (4) complying with work requirements for other federal programs, (5) participating in a drug or alcohol treatment and rehabilitation program, or (6) enrolled at least half-time in school.</p>",
      "updateDate": "2025-06-13",
      "versionCode": "id119hr1279"
    },
    "title": "To amend title XIX of the Social Security Act to establish a community engagement requirement for certain individuals under the Medicaid program."
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill establishes community engagement requirements (i.e., work requirements) for certain adults under Medicaid.</p><p>Specifically, the bill requires individuals ages 18 through 65 to work, engage in community service, or participate in a work program (or a combination of these) for at least 80 hours per month. The bill prohibits federal payments for, and allows state Medicaid programs to disenroll, individuals who do not meet these requirements for three or more months in a year.</p><p>The requirements do not apply to individuals who are (1) physically or mentally unfit to work, (2) pregnant, (3) parents or caretakers of children or incapacitated individuals, (4) complying with work requirements for other federal programs, (5) participating in a drug or alcohol treatment and rehabilitation program, or (6) enrolled at least half-time in school.</p>",
      "updateDate": "2025-06-13",
      "versionCode": "id119hr1279"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1279ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XIX of the Social Security Act to establish a community engagement requirement for certain individuals under the Medicaid program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-14T09:18:21Z"
    },
    {
      "title": "To amend title XIX of the Social Security Act to establish a community engagement requirement for certain individuals under the Medicaid program.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-14T09:05:52Z"
    }
  ]
}
```
