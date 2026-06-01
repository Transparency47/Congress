# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2686?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2686
- Title: University Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 2686
- Origin chamber: House
- Introduced date: 2025-04-07
- Update date: 2025-05-09T16:46:02Z
- Update date including text: 2025-05-09T16:46:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-07: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-04-07: Introduced in House

## Actions

- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Introduced in House
- 2025-04-07 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-07",
    "latestAction": {
      "actionDate": "2025-04-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2686",
    "number": "2686",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M000317",
        "district": "11",
        "firstName": "Nicole",
        "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
        "lastName": "Malliotakis",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "University Accountability Act",
    "type": "HR",
    "updateDate": "2025-05-09T16:46:02Z",
    "updateDateIncludingText": "2025-05-09T16:46:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-07",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-07",
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
          "date": "2025-04-07T16:03:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2686ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2686\nIN THE HOUSE OF REPRESENTATIVES\nApril 7, 2025 Ms. Malliotakis (for herself, Ms. Stefanik , and Ms. Tenney ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to impose penalties with respect to civil rights violations by certain tax-exempt educational institutions.\n#### 1. Short title\nThis Act may be cited as the University Accountability Act .\n#### 2. Penalties with respect to civil rights violations by certain tax-exempt educational institutions\n##### (a) In general\nPart I of subchapter B of chapter 68 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n6720D. Civil rights violations by certain tax-exempt educational institutions (a) In general There is hereby imposed a penalty equal to the applicable penalty amount on a specified tax-exempt educational institution with respect to each determination of civil rights violation with respect to such institution. (b) Timing of liability (1) In general A specified tax-exempt educational institution shall be liable for the penalty imposed under subsection (a) with respect to any determination of civil rights violation on the date of the judgment referred to in subsection (c). (2) Reversal of determinations In the event that any determination of civil rights violation is vacated, overturned, or otherwise reversed, the Secretary shall refund any penalty paid with respect to the determination of civil rights violation. The preceding sentence shall not be interpreted to prevent the application of this section with respect to any determination of civil rights violation that is reinstated or otherwise redetermined following any such reversal. (c) Determination of civil rights violation For purposes of this section\u2014 (1) In general The term determination of civil rights violation means, with respect to any specified tax-exempt educational institution, any civil judgment of a Federal court of competent jurisdiction that such institution violated any provision of title VI of the Civil Rights Act of 1964. (2) Authority to treat certain judgments as a single determination of civil rights violation If the Secretary determines that two or more judgments are based on the same set of facts and circumstances, such judgments shall be treated as a single determination of civil rights violation for purposes of this section, section 501(s), and such provisions of section 6033(o) as the Secretary determines appropriate. (d) Applicable penalty amount For purposes of this section\u2014 (1) In general The term applicable penalty amount means, with respect to each determination of civil rights violation made with respect to any specified tax-exempt educational institution, the greater of\u2014 (A) $100,000, or (B) in the case of an institution subject to the requirements of section 6033(a), 5 percent of the aggregate administrative compensation paid by such specified tax-exempt educational institution during the taxable year in which such violation occurred. (2) Administrative compensation The term administrative compensation means, with respect to any specified tax-exempt educational institution, the compensation and other payments described in section 6033(b)(7) made by such institution. (e) Specified tax-Exempt educational institution For purposes of this section, the term specified tax-exempt educational institution means any eligible educational institution (as defined in section 25A(f)(2)) which is described in section 501(c) or section 511(a)(2)(B). (f) Waiver of limitations on assessment and refund Sections 6501 and 6511 shall not apply to any penalty imposed under subsection (a) or refund made under subsection (b)(2). .\n##### (b) Mandatory review of exempt status upon repeated civil rights violations\nSection 501 of such Code is amended by adding at the end the following new subsection:\n(s) Mandatory review of exempt status of certain educational institutions with repeated civil rights violations Upon any determination of civil right violation (as defined in section 6720D(c)) with respect to any specified tax-exempt educational institution (as defined in section 6720D(e)), if such determination is not one of the first 2 such determinations (made after the date of the enactment of this subsection) with respect to such institution, the Secretary shall conduct a review to determine if such institution remains an organization described in subsection (c) which is entitled to exemption from tax under subsection (a). Any determination which is vacated, overturned, or otherwise reversed shall not be taken into account under the preceding sentence (unless subsequently reinstated or otherwise redetermined). .\n##### (c) Reporting by specified tax-Exempt educational institutions of determinations of civil rights violation\nSection 6033 of such Code is amended by redesignating subsection (o) as subsection (p) and by inserting after subsection (n) the following new subsection:\n(o) Additional provisions relating to specified tax-Exempt educational institutions (1) In general Every specified tax-exempt educational institution (as defined in section 6720D(c)) which is subject to the requirements of subsection (a) shall, on the return required under subsection (a) for the taxable year, include the following: (A) With respect to each determination of civil rights violation (as defined in section 6720D(c)) made with respect to such institution during such taxable year: (i) A description of such determination (including the date of such determination) and of the civil rights violation to which such determination relates. (ii) The number of determinations of civil rights violation (determined by disregarding determinations not taken into account under the last sentence of section 501(s)) made with respect to such institution before such determination (and after the date of the enactment of this subsection). (iii) Such other information as the Secretary may require. (B) With respect to each determination of civil rights violation (as defined in section 6720D(c)) which is vacated, overturned, or otherwise reversed during such taxable year: (i) A description of the order or judgment which so reversed such determination, including the date of such order or judgment. (ii) The information described in subparagraph (A)(i) with respect to the determination so reversed. (iii) Such other information as the Secretary may require. (2) Application to State colleges and universities Every specified tax-exempt educational institution (as defined in section 6720D(c)) which is described in section 511(a)(2)(B) shall, for any taxable year with respect to which there is a determination of civil rights violation described in subparagraph (A) or (B) of paragraph (1) with respect to such institution, file an annual return that contains the information described in such subparagraphs. The penalties applicable to returns required under subsection (a) shall apply to returns required under this paragraph. .\n##### (d) Clerical amendment\nThe table of sections for part I of subchapter B of chapter 68 of such Code is amended by adding at the end the following new item:\nSec. 6720D. Civil rights violations by certain tax-exempt educational institutions. .\n##### (e) Effective date\nThe amendments made by this subsection shall apply with respect to determinations of civil rights violation made after the date of the enactment of this Act.",
      "versionDate": "2025-04-07",
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
        "name": "Taxation",
        "updateDate": "2025-05-09T16:46:02Z"
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
      "date": "2025-04-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2686ih.xml"
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
      "title": "University Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-16T02:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "University Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-16T02:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to impose penalties with respect to civil rights violations by certain tax-exempt educational institutions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-16T02:48:26Z"
    }
  ]
}
```
