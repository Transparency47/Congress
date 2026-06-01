# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8635?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8635
- Title: VERIFY Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8635
- Origin chamber: House
- Introduced date: 2026-04-30
- Update date: 2026-05-19T22:02:48Z
- Update date including text: 2026-05-19T22:02:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-04-30: Introduced in House

## Actions

- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8635",
    "number": "8635",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "S001229",
        "district": "6",
        "firstName": "Jefferson",
        "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
        "lastName": "Shreve",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "VERIFY Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-19T22:02:48Z",
    "updateDateIncludingText": "2026-05-19T22:02:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-30",
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
      "actionDate": "2026-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T13:04:05Z",
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
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David J. [R-OH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8635ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8635\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2026 Mr. Shreve (for himself and Mr. Taylor ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo modernize and improve the accuracy, timeliness, and interoperability of the Systematic Alien Verification for Entitlements program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Verification Enhancement and Reliability for Immigration Fidelity Act of 2026 or as the VERIFY Act of 2026 .\n#### 2. SAVE program modernization\n##### (a) General requirement\nThe Secretary of Homeland Security, acting through United States Citizenship and Immigration Services, shall modernize the SAVE program to ensure accurate, timely, and reliable verification response, including by\u2014\n**(1)**\nupgrading query processing infrastructure to reduce response latency;\n**(2)**\nimplementing automated data reconciliation with source systems;\n**(3)**\nexpanding API access for authorized querying agencies; and\n**(4)**\nestablishing a user feedback mechanism for agencies to report suspected data errors.\n##### (b) Timeliness of updates\nTo the maximum extent practicable and consistent with applicable law, the Secretary shall ensure that changes to an individual\u2019s immigration status, including grants, extensions, expirations, revocations, or terminations of lawful status or parole, are reflected in the SAVE program not later than 24 hours after such changes are recorded in the originating system.\n##### (c) Interoperability and data sharing\nThe Secretary, consistent with the Privacy Act of 1974, the E-Government Act of 2002, the Computer Matching and Privacy Protection Act of 1988, and other applicable Federal law, shall\u2014\n**(1)**\nintegrate the SAVE program into relevant Department of Homeland Security systems, including arrival and departure information systems;\n**(2)**\nestablish or update memoranda of understanding with the Social Security Administration and other Federal agencies, as appropriate, to improve verification accuracy using data-sharing arrangements authorized under applicable Federal law, including section 6103 of the Internal Revenue Code, the Computer Matching and Privacy Protection Act of 1988, and memoranda of understanding in effect as of the date of enactment of this Act; and\n**(3)**\nencourage voluntary data-sharing agreements with State vital records agencies for verification of birth and death information, where legally permissible.\n##### (d) Post-Verification status change alerts\nThe SAVE program shall notify querying agencies when an individual\u2019s immigration status materially changes after a prior verification, when such notification is relevant to continued eligibility. Notifications shall comply with privacy applicable Federal privacy laws, including the Privacy Act of 1974, and with additional administrative safeguards established by the Secretary and include only information necessary for eligibility determinations.\n##### (e) Data scope limitations\nInformation used or displayed through the SAVE program shall be limited to data necessary for eligibility verification purposes. Nothing in this Act may be construed to authorize\u2014\n**(1)**\nthe expansion of the SAVE program to include non-immigration criminal history databases; and\n**(2)**\nthe use of the SAVE program for general law enforcement or surveillance purposes.\n##### (f) Use of automated tools\nThe Secretary may use automated or algorithmic tools within the SAVE program solely for data reconciliation, error reduction, and identity matching, provided that\u2014\n**(1)**\nno adverse eligibility determination is made solely on the basis of automated processing;\n**(2)**\nhuman review is required for contested or negative determinations; and\n**(3)**\nthe Secretary implements regular testing for accuracy and bias and submits summary results annually to Congress.\n#### 3. Prohibition on user access and fees\nNo fee may be charged to a Federal, State, local, or Tribal government agency for submitting a verification query through the SAVE program.\n#### 4. Implementation and oversight\n##### (a) Modernization plan\nNot later than 180 days after enactment of this Act, the Secretary shall submit to Congress a SAVE modernization plan that includes\u2014\n**(1)**\na description of technological upgrades to the SAVE program;\n**(2)**\nuser training improvements; and\n**(3)**\nperformance metrics related to accuracy and response time, including error rates and average query completion time benchmarks.\n##### (b) Inspector general audits\nThe Inspector General of the Department of Homeland Security shall conduct annual audits of the SAVE program\u2019s accuracy, timeliness, and compliance with this Act, and submit reports to Congress.\n##### (c) Corrective action\nIf the Inspector General identifies material non-compliance, the Secretary shall submit a corrective action plan to Congress within 90 days. Continued non-compliance may be addressed through limitations on the use of funds for non-SAVE discretionary activities, as determined by Congress, and may trigger suspension of SAVE queries until compliance is restored.\n#### 5. Definition\nFor purposes of this Act, the term SAVE program means the Systematic Alien Verification for Entitlements program, established pursuant to section 121 of the Immigration Reform and Control Act of 1986.\n#### 6. Effective date\nThis Act shall take effect one year after the date of enactment, except that planning and reporting requirements under section 4 shall take effect immediately upon enactment.\n#### 7. Severability\nIf any provision of this Act, or the application thereof, is held invalid, the remainder of this Act shall not be affected.",
      "versionDate": "2026-04-30",
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
        "name": "Immigration",
        "updateDate": "2026-05-19T22:02:47Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8635ih.xml"
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
      "title": "VERIFY Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-08T10:08:45Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "VERIFY Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T10:08:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Verification Enhancement and Reliability for Immigration Fidelity Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T10:08:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To modernize and improve the accuracy, timeliness, and interoperability of the Systematic Alien Verification for Entitlements program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-08T10:03:32Z"
    }
  ]
}
```
