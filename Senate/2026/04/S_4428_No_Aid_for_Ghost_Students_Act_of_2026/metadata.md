# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4428?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4428
- Title: No Aid for Ghost Students Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4428
- Origin chamber: Senate
- Introduced date: 2026-04-29
- Update date: 2026-05-21T15:00:33Z
- Update date including text: 2026-05-21T15:00:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-29: Introduced in Senate
- 2026-04-29 - IntroReferral: Introduced in Senate
- 2026-04-29 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-04-29: Introduced in Senate

## Actions

- 2026-04-29 - IntroReferral: Introduced in Senate
- 2026-04-29 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-29",
    "latestAction": {
      "actionDate": "2026-04-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4428",
    "number": "4428",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "M001244",
        "district": "",
        "firstName": "Ashley",
        "fullName": "Sen. Moody, Ashley [R-FL]",
        "lastName": "Moody",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "No Aid for Ghost Students Act of 2026",
    "type": "S",
    "updateDate": "2026-05-21T15:00:33Z",
    "updateDateIncludingText": "2026-05-21T15:00:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
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
      "actionDate": "2026-04-29",
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
          "date": "2026-04-29T16:47:33Z",
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
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "NH"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4428is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4428\nIN THE SENATE OF THE UNITED STATES\nApril 29, 2026 Mrs. Moody (for herself, Ms. Hassan , and Mr. Tuberville ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Higher Education Act of 1965 to require the use of an identity fraud detection system in reviewing Free Applications for Federal Student Aid.\n#### 1. Short title\nThis Act may be cited as the No Aid for Ghost Students Act of 2026 .\n#### 2. Identity fraud detection system\n##### (a) Identity fraud detection system\nSection 483 of the Higher Education Act of 1965 ( 20 U.S.C. 1090 ) is amended by adding at the end the following:\n(e) Identity fraud detection system (1) In general In addition to or in conjunction with other verification processes carried out under this title, the Secretary shall use an identity fraud detection system to review each application submitted under this section on or after October 1, 2026, to determine whether the application presents a reasonable suspicion of identity fraud. If the Secretary determines that such an application presents a reasonable suspicion of identity fraud, the Secretary shall carry out notifications in accordance with paragraph (2). (2) Notification of reasonable suspicion of identity fraud If the Secretary determines that an application submitted under this section presents a reasonable suspicion of identity fraud, the Secretary shall\u2014 (A) provide the applicant with notice\u2014 (i) of such determination and the basis for such determination; (ii) that the information described in subparagraph (B) will be transmitted to each institution of higher education designated by the applicant in the application; and (iii) that the applicant is subject to additional identity verification requirements in accordance with section 487(a)(15); and (B) transmit to each institution designated by the applicant in the application, a notice\u2014 (i) that such application presents a reasonable suspicion of identity fraud; and (ii) that the applicant is subject to identity verification requirements to be carried out by the institution in accordance with section 487(a)(15)(B), before the institution may disburse Federal financial aid under this title to such applicant. (3) Congressional notices and report (A) Notices The Secretary shall submit to the authorizing committees\u2014 (i) not later than November 1, 2026, a written description of the identity fraud detection system required under this subsection; and (ii) not later than 30 days after implementing any substantial change to such system, a written description and rationale for such change. (B) Annual evaluation and report Not later than October 1, 2027, and annually thereafter, the Secretary shall conduct an evaluation of the effectiveness of the identity fraud detection system carried out under this subsection, and submit to the authorizing committees a report on the use and effectiveness of such system. .\n##### (b) Additional verification requirements\n**(1) Amendments**\nSection 487(a)(15) of the Higher Education Act of 1965 ( 20 U.S.C. 1094(a)(15) ) is amended\u2014\n**(A)**\nby striking (15) The institution acknowledges and inserting (15)(A) The institution acknowledges ; and\n**(B)**\nby adding at the end the following new subparagraph:\n(B) Beginning on October 1, 2026, the institution will not disburse Federal financial aid under this title to an applicant whose application under section 483 presents a reasonable suspicion of identity fraud under section 483(e), unless the institution, in accordance with procedures established by the Secretary\u2014 (i) determines that a reasonable suspicion of identity fraud is not present by confirming the identity of such applicant using in-person verification or live, synchronous audiovisual verification; (ii) notifies the Secretary that the identity of the applicant has been verified; and (iii) maintains a record of such identity verification. .\n**(2) Guidelines on institutional verification procedures**\nNot later than October 1, 2026, the Secretary of Education shall establish guidelines with respect to identity verification procedures to be carried out by institutions of higher education under subparagraph (B) of section 487(a)(15) of the Higher Education Act of 1965 ( 20 U.S.C. 1094(a)(15) ), as amended by paragraph (1).",
      "versionDate": "2026-04-29",
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
        "actionDate": "2026-03-17",
        "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 30 - 3."
      },
      "number": "7892",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "No Aid for Ghost Students Act of 2026",
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
        "name": "Education",
        "updateDate": "2026-05-21T15:00:33Z"
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
      "date": "2026-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4428is.xml"
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
      "title": "No Aid for Ghost Students Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-09T05:23:46Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Aid for Ghost Students Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-09T05:23:45Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Higher Education Act of 1965 to require the use of an identity fraud detection system in reviewing Free Applications for Federal Student Aid.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-09T05:18:39Z"
    }
  ]
}
```
