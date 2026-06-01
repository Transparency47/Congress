# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8126?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8126
- Title: Congressional Accountability Act Enhancement Act
- Congress: 119
- Bill type: HR
- Bill number: 8126
- Origin chamber: House
- Introduced date: 2026-03-26
- Update date: 2026-05-20T08:08:16Z
- Update date including text: 2026-05-20T08:08:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2026-03-26: Introduced in House

## Actions

- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8126",
    "number": "8126",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "S001205",
        "district": "5",
        "firstName": "Mary Gay",
        "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
        "lastName": "Scanlon",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Congressional Accountability Act Enhancement Act",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:16Z",
    "updateDateIncludingText": "2026-05-20T08:08:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T14:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "IL"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "DC"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "DE"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8126ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8126\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2026 Ms. Scanlon (for herself and Ms. Underwood ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo amend the Congressional Accountability Act of 1995 to require Members of Congress to reimburse the Treasury for amounts paid as settlements and awards under such Act in all cases of employment discrimination acts committed personally by Members, to permit individuals who file claims under such Act to file an amended claim if the preliminary review of the individual\u2019s claim by a hearing officer includes the determination that the individual filing the claim is not a covered employee under such Act or has not stated a claim for which relief may be granted under title IV of such Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Congressional Accountability Act Enhancement Act .\n#### 2. Revision of rules requiring reimbursement for amounts paid as settlements and awards under Congressional Accountability Act of 1995 in cases of employment discrimination\n##### (a) Requiring Members of Congress To reimburse Treasury for amounts paid as settlements and awards in all cases of employment discrimination acts by Members\n**(1) Requiring reimbursement**\nClause (i) of section 415(d)(1)(C) of the Congressional Accountability Act of 1995 ( 2 U.S.C. 1415(d)(1)(C) ) is amended to read as follows:\n(i) a violation of section 201(a) or section 206(a); or .\n**(2) Conforming amendment relating to notification of possibility of reimbursement**\nClause (i) of section 402(b)(2)(B) of the Congressional Accountability Act of 1995 ( 2 U.S.C. 1402(b)(2)(B) ) is amended to read as follows:\n(i) a violation of section 201(a) or section 206(a); or .\n##### (b) Requiring other employing offices To reimburse Treasury for amounts paid in claims involving retaliation for filing employment discrimination claim\nSection 415(e) of such Act ( 2 U.S.C. 1415(e) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking a violation of section 201(a) or 206(a) and inserting a violation described in paragraph (4) ; and\n**(2)**\nby adding at the end the following new paragraph:\n(4) Violations described A violation described in this paragraph is\u2014 (A) a violation of section 201(a) or 206(a); or (B) intimidation, reprisal, or discrimination that is unlawful under section 207 and is taken against a covered employee because of a claim alleging a violation described in subparagraph (A). .\n##### (c) Effective date\nThe amendments made by this section shall apply with respect to claims under the Congressional Accountability Act of 1995 which are made on or after the date of the enactment of this Act.\n#### 3. Permitting individuals filing claims under Congressional Accountability Act of 1995 to file amended claims if preliminary review includes determination of failure to state claim for which relief may be granted\n##### (a) Permitting filing of amended claims\nSection 403(d) of the Congressional Accountability Act of 1995 ( 2 U.S.C. 1402a(d) ) is amended to read as follows:\n(d) Effect of Determination of Failure To State Claim for Which Relief May Be Granted (1) Permitting filing of amended version of claim If the hearing officer\u2019s report on the preliminary review of a claim under subsection (c) includes the determination that the individual filing the claim is not a covered employee or has not stated a claim for which relief may be granted under this title\u2014 (A) the individual may file an amended version of the claim under this section; and (B) the amended claim shall be subject to a preliminary review under this section in the same manner as the original version of the claim. (2) Effect of determination If the individual does not file an amended claim under paragraph (1)(A) prior to the expiration of the 10-day period which begins on the date the hearing officer submits the report on the preliminary review of the individual\u2019s original version of the claim under subsection (c), or if the hearing officer\u2019s report on the amended version of the claim includes the determination that the individual filing the claim is not a covered employee or has not stated a claim for which relief may be granted under this title\u2014 (A) the individual (including an individual who is a Library claimant, as defined in section 401(d)(1)) may not obtain a formal hearing with respect to the claim as provided under section 405; and (B) the hearing officer shall provide the individual and the Executive Director with a written notice that the individual may file a civil action with respect to the claim in accordance with section 408. .\n##### (b) Effective date\nThe amendments made by this section shall apply with respect to claims under the Congressional Accountability Act of 1995 which are made on or after the date of the enactment of this Act.\n#### 4. Permitting Office of Employee Advocacy to provide assistance to covered employees in connection with civil actions\n##### (a) In general\nNotwithstanding section 724(c) of House Resolution 724, One Hundred Fifteenth Congress, if a covered employee of the House of Representatives under the Congressional Accountability Act of 1995 files a civil action with respect to an alleged violation of such Act, as provided in section 408 of such Act, the Office of Employee Advocacy may provide assistance to the employee with respect to investigations or proceedings under such Act in connection with such alleged violation at any time, including after the employee files such action.\n##### (b) Exercise of rulemaking authority\nThis section is enacted by Congress\u2014\n**(1)**\nas an exercise of the rulemaking power of the House of Representatives, and as such it is deemed a part of the rules of the House of Representatives, and it supersedes other rules only to the extent that it is inconsistent with such rules; and\n**(2)**\nwith full recognition of the constitutional right of the House of Representatives to change the rules (so far as relating to the procedure of the House) at any time, in the same manner, and to the same extent as in the case of any other rule of the House.",
      "versionDate": "2026-03-26",
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
        "name": "Congress",
        "updateDate": "2026-04-14T19:33:05Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8126ih.xml"
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
      "title": "Congressional Accountability Act Enhancement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-11T03:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Congressional Accountability Act Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-11T03:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Congressional Accountability Act of 1995 to require Members of Congress to reimburse the Treasury for amounts paid as settlements and awards under such Act in all cases of employment discrimination acts committed personally by Members, to permit individuals who file claims under such Act to file an amended claim if the preliminary review of the individual's claim by a hearing officer includes the determination that the individual filing the claim is not a covered employee under such Act or has not stated a claim for which relief may be granted under title IV of such Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-11T03:48:36Z"
    }
  ]
}
```
