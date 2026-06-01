# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3430?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3430
- Title: SRO Funding Protection Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3430
- Origin chamber: House
- Introduced date: 2025-05-15
- Update date: 2025-07-21T19:44:15Z
- Update date including text: 2025-07-21T19:44:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-05-15: Introduced in House

## Actions

- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3430",
    "number": "3430",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "B001301",
        "district": "1",
        "firstName": "Jack",
        "fullName": "Rep. Bergman, Jack [R-MI-1]",
        "lastName": "Bergman",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "SRO Funding Protection Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-21T19:44:15Z",
    "updateDateIncludingText": "2025-07-21T19:44:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-15",
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
          "date": "2025-05-15T14:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3430ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3430\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2025 Mr. Bergman (for himself and Mr. Huizenga ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Elementary and Secondary Education Act of 1965 to require maintenance of State funds for school resource officers in elementary schools and secondary schools, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the School Resource Officer Funding Protection Act of 2025 or the SRO Funding Protection Act of 2025 .\n#### 2. School resource officer funding\nSubpart 2 of part F of title VIII of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7901 et seq. ) is amended by adding at the end the following:\n8549D. School resource officer funding maintenance (a) In general Beginning with the first fiscal year beginning after the date of the enactment of this section, a State educational agency may receive the total amount of funds that the agency is eligible to receive under a program under this Act for any fiscal year only if the agency maintains funding for school resource officer programs in elementary schools and secondary schools served by the agency at an amount that is not less than the greater of\u2014 (1) the amount expended by the agency for such school resource officer programs in the most recent fiscal year preceding such fiscal year in which the agency, as applicable\u2014 (A) did not receive a waiver under subsection (d); or (B) complied with the requirements of this section; or (2) the average annual amount expended by the agency for such school resource programs during the 5 fiscal years immediately preceding such fiscal year. (b) Report A State educational agency shall, on an annual basis, submit to the Secretary a certification of compliance with the requirement under subsection (a) in such form, at such time, and containing such information as the Secretary may require, including a public report detailing, for the fiscal year in which the report is submitted and each of the 5 preceding fiscal years\u2014 (1) the amount of State funding for school resource officer programs in elementary schools and secondary schools served by the agency; and (2) the number of school resource officers working in such elementary schools and secondary schools pursuant to such programs. (c) Noncompliance In the case of a State educational agency that fails to meet the requirement under subsection (a) for a fiscal year and does not receive a waiver under subsection (d), the Secretary shall, for the following fiscal year, reduce the total amount of funds that the agency is eligible to receive under programs under this Act in such following fiscal year by an amount in proportion to\u2014 (1) the amount of State funding for school resource officer programs in elementary schools and secondary schools served by the agency for the fiscal year in which the agency fails to meet such requirement; compared to (2) the amount of such funding expended by the agency in the most recent fiscal year preceding such fiscal year in which the agency, as applicable\u2014 (A) did not receive a waiver under subsection (d); or (B) complied with the requirements of this section. (d) Waiver The Secretary may waive the requirements under subsection (a) for a State educational agency that submits to the Secretary a waiver request demonstrating that extraordinary financial circumstances of the State, including but not limited to significant economic downturn or natural disaster, resulted in a reduction in the amount of State funding for school resource officer programs in elementary schools and secondary schools served by the agency. (e) School resource officer defined For purposes of this section, the term school resource officer has the meaning given such term in section 1709 of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10389 ). .",
      "versionDate": "2025-05-15",
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
        "name": "Education",
        "updateDate": "2025-05-29T15:22:13Z"
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
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3430ih.xml"
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
      "title": "SRO Funding Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-27T04:23:43Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SRO Funding Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-27T04:23:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "School Resource Officer Funding Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-27T04:23:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Elementary and Secondary Education Act of 1965 to require maintenance of State funds for school resource officers in elementary schools and secondary schools, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-27T04:18:22Z"
    }
  ]
}
```
