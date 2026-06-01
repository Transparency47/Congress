# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3400?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3400
- Title: Ally’s Act
- Congress: 119
- Bill type: S
- Bill number: 3400
- Origin chamber: Senate
- Introduced date: 2025-12-09
- Update date: 2026-04-15T11:03:26Z
- Update date including text: 2026-04-15T11:03:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-09: Introduced in Senate
- 2025-12-09 - IntroReferral: Introduced in Senate
- 2025-12-09 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-12-09: Introduced in Senate

## Actions

- 2025-12-09 - IntroReferral: Introduced in Senate
- 2025-12-09 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-09",
    "latestAction": {
      "actionDate": "2025-12-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3400",
    "number": "3400",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001114",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Curtis, John R. [R-UT]",
        "lastName": "Curtis",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Ally\u2019s Act",
    "type": "S",
    "updateDate": "2026-04-15T11:03:26Z",
    "updateDateIncludingText": "2026-04-15T11:03:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-09",
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
      "actionDate": "2025-12-09",
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
        "item": [
          {
            "date": "2025-12-09T20:13:06Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-09T20:13:06Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "MA"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "WV"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "CO"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "GA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-02-05",
      "state": "NJ"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "IL"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "NH"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "MN"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "NJ"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "CT"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "ME"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "GA"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "MD"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3400is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3400\nIN THE SENATE OF THE UNITED STATES\nDecember 9, 2025 Mr. Curtis (for himself, Ms. Warren , Mrs. Capito , Mr. Hickenlooper , and Mr. Warnock ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend title XXVII of the Public Health Service Act, the Employee Retirement Income Security Act of 1974, the Internal Revenue Code of 1986, and the Patient Protection and Affordable Care Act to require coverage of hearing devices and systems in certain private health insurance plans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as Ally\u2019s Act .\n#### 2. Coverage of hearing devices and systems in certain private health insurance plans\n##### (a) PHSA\nPart D of the Public Health Service Act ( 42 U.S.C. 300gg\u2013111 et seq. ) is amended by adding at the end the following new section:\n2799A\u201311. Coverage of hearing devices and systems (a) In general A group health plan and a health insurance issuer offering group or individual health insurance coverage shall at a minimum provide coverage for the following items and services furnished to a qualifying individual: (1) Auditory implant devices (including auditory osseointegrated (bone conduction) implants and cochlear implants) and external sound processors. (2) The maintenance of auditory implant devices and external sound processors described in paragraph (1). (3) Every 5 years, the upgrade (or replacement if an upgrade is not available) of auditory implant devices and external sound processors described in paragraph (1). (4) Adhesive adapters and softband headbands. (5) The repair of auditory implant devices and external sound processors described in paragraph (1). (6) A comprehensive hearing assessment. (7) A preoperative medical assessment. (8) Surgery relating to the furnishing of such devices and processors (as determined necessary by a physician or qualified audiologist (as such terms are defined in subsection (d)) treating such individual). (9) Postoperative medical visits for purposes of ensuring appropriate recovery from such surgery. (10) Postoperative audiological visits for activation and fitting of such devices and processors. (11) Aural rehabilitation and treatment services (as so determined necessary). (b) Coverage requirements In the case of an item or service described in subsection (a) furnished to a qualifying individual under a group health plan or group or individual health insurance coverage, such plan or coverage shall ensure that\u2014 (1) the financial requirements (as defined in section 2726(a)(3)) applicable to such item or service are no more restrictive than the predominant financial requirements applied to substantially all medical and surgical benefits covered by the plan or coverage (as applicable), and that there are no separate cost sharing requirements that are applicable only with respect to such item or service; and (2) the treatment limitations (as defined in such section) applicable to such item or service are no more restrictive than the predominant treatment limitations applied to substantially all medical and surgical benefits covered by the plan or coverage (as applicable), and that there are no separate treatment limitations that are applicable only with respect to such item or service. (c) Prohibition on review of medical necessity A group health plan and a health insurance issuer offering group or individual health insurance coverage may not deny or otherwise limit coverage of any item or service described in subsection (a) where such item or service has been determined to be medically necessary by a physician or qualified audiologist (as such terms are defined in subsection (d)). (d) Qualifying individual defined For purposes of this section, the term qualifying individual means an individual that a physician (as defined in section 1861(r) of the Social Security Act) or qualified audiologist (as defined in section 1861(ll)(4)(B) of such Act) determines meets an indication (including unilateral or bilateral hearing loss) for an auditory implant device and external sound processor described in subsection (a)(1). .\n##### (b) ERISA\n**(1) In general**\nSubpart B of part 7 of subtitle B of title I of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1185 et seq. ) by adding at the end the following new section:\n726. Coverage of hearing devices and systems (a) In general A group health plan and a health insurance issuer offering group health insurance coverage shall at a minimum provide coverage for the following items and services furnished to a qualifying individual: (1) Auditory implant devices (including auditory osseointegrated (bone conduction) implants and cochlear implants) and external sound processors. (2) The maintenance of auditory implant devices and external sound processors described in paragraph (1). (3) Every 5 years, the upgrade (or replacement if an upgrade is not available) of auditory implant devices and external sound processors described in paragraph (1). (4) Adhesive adapters and softband headbands. (5) The repair of auditory implant devices and external sound processors described in paragraph (1). (6) A comprehensive hearing assessment. (7) A preoperative medical assessment. (8) Surgery relating to the furnishing of such devices and processors (as determined necessary by a physician or qualified audiologist (as such terms are defined in subsection (d)) treating such individual). (9) Postoperative medical visits for purposes of ensuring appropriate recovery from such surgery. (10) Postoperative audiological visits for activation and fitting of such devices and processors. (11) Aural rehabilitation and treatment services (as so determined necessary). (b) Coverage requirements In the case of an item or service described in subsection (a) furnished to a qualifying individual under a group health plan or group health insurance coverage, such plan or coverage shall ensure that\u2014 (1) the financial requirements (as defined in section 712(a)(3)) applicable to such item or service are no more restrictive than the predominant financial requirements applied to substantially all medical and surgical benefits covered by the plan or coverage (as applicable), and that there are no separate cost sharing requirements that are applicable only with respect to such item or service; and (2) the treatment limitations (as defined in such section) applicable to such item or service are no more restrictive than the predominant treatment limitations applied to substantially all medical and surgical benefits covered by the plan or coverage (as applicable), and that there are no separate treatment limitations that are applicable only with respect to such item or service. (c) Prohibition on review of medical necessity A group health plan and a health insurance issuer offering group health insurance coverage may not deny or otherwise limit coverage of any item or service described in subsection (a) where such item or service has been determined to be medically necessary by a physician or qualified audiologist (as such terms are defined in subsection (d)). (d) Qualifying individual defined For purposes of this section, the term qualifying individual means an individual that a physician (as defined in section 1861(r) of the Social Security Act ( 42 U.S.C. 1395x(r) )) or qualified audiologist (as defined in section 1861(ll)(4)(B) of such Act ( 42 U.S.C. 1395x(ll)(4)(B) )) determines meets an indication (including unilateral or bilateral hearing loss) for an auditory implant device and external sound processor described in subsection (a)(1). .\n**(2) Clerical amendment**\nThe table of contents in section 1 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1001 et seq. ) is amended by inserting after the item relating to section 725 the following new item:\nSec. 726. Coverage of hearing devices and systems. .\n##### (c) IRC\n**(1) In general**\nSubchapter B of chapter 100 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n9826. Coverage of hearing devices and systems (a) In general A group health plan shall at a minimum provide coverage for the following items and services furnished to a qualifying individual: (1) Auditory implant devices (including auditory osseointegrated (bone conduction) implants and cochlear implants) and external sound processors. (2) The maintenance of auditory implant devices and external sound processors described in paragraph (1). (3) Every 5 years, the upgrade (or replacement if an upgrade is not available) of auditory implant devices and external sound processors described in paragraph (1). (4) Adhesive adapters and softband headbands. (5) The repair of auditory implant devices and external sound processors described in paragraph (1). (6) A comprehensive hearing assessment. (7) A preoperative medical assessment. (8) Surgery relating to the furnishing of such devices and processors (as determined necessary by a physician or qualified audiologist (as such terms are defined in subsection (d)) treating such individual). (9) Postoperative medical visits for purposes of ensuring appropriate recovery from such surgery. (10) Postoperative audiological visits for activation and fitting of such devices and processors. (11) Aural rehabilitation and treatment services (as so determined necessary). (b) Coverage requirements In the case of an item or service described in subsection (a) furnished to a qualifying individual under a group health plan, such plan shall ensure that\u2014 (1) the financial requirements (as defined in section 9812(a)(3)) applicable to such item or service are no more restrictive than the predominant financial requirements applied to substantially all medical and surgical benefits covered by the plan, and that there are no separate cost sharing requirements that are applicable only with respect to such item or service; and (2) the treatment limitations (as defined in such section) applicable to such item or service are no more restrictive than the predominant treatment limitations applied to substantially all medical and surgical benefits covered by the plan, and that there are no separate treatment limitations that are applicable only with respect to such item or service. (c) Prohibition on review of medical necessity A group health plan may not deny or otherwise limit coverage of any item or service described in subsection (a) where such item or service has been determined to be medically necessary by a physician or qualified audiologist (as such terms are defined in subsection (d)). (d) Qualifying individual defined For purposes of this section, the term qualifying individual means an individual that a physician (as defined in section 1861(r) of the Social Security Act ( 42 U.S.C. 1395x(r) )) or qualified audiologist (as defined in section 1861(ll)(4)(B) of such Act ( 42 U.S.C. 1395x(ll)(4)(B) )) determines meets an indication (including unilateral or bilateral hearing loss) for an auditory implant device and external sound processor described in subsection (a)(1). .\n**(2) Clerical amendment**\nThe table of sections for subchapter B of chapter 100 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 9825 the following new item:\nSec. 9286. Coverage of hearing devices and systems. .\n##### (d) Application to grandfathered health plans\nSection 1251(a)(4)(A) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18011(a)(4)(A) ) is amended\u2014\n**(1)**\nby striking title and inserting title, or as added after the date of the enactment of this Act ; and\n**(2)**\nby adding at the end the following new clause:\n(v) Section 2799A\u201311 (relating to hearing devices and systems). .\n##### (e) Effective date\nThe amendments made by this section shall apply with respect to plan years beginning on or after January 1, 2026.",
      "versionDate": "2025-12-09",
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
        "actionDate": "2025-07-22",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Education and Workforce, and Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4606",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Ally\u2019s Act",
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
        "name": "Health",
        "updateDate": "2026-01-07T16:18:21Z"
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
      "date": "2025-12-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3400is.xml"
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
      "title": "Ally\u2019s Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-15T11:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Ally\u2019s Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-31T03:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XXVII of the Public Health Service Act, the Employee Retirement Income Security Act of 1974, the Internal Revenue Code of 1986, and the Patient Protection and Affordable Care Act to require coverage of hearing devices and systems in certain private health insurance plans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-31T03:33:14Z"
    }
  ]
}
```
