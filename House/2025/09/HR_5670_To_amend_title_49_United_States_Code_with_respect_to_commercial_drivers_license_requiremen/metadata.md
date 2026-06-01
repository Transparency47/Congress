# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5670?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5670
- Title: Protecting America’s Roads Act
- Congress: 119
- Bill type: HR
- Bill number: 5670
- Origin chamber: House
- Introduced date: 2025-09-30
- Update date: 2025-12-10T19:31:54Z
- Update date including text: 2025-12-10T19:31:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-30: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-30 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-01 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-09-30: Introduced in House

## Actions

- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-30 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-01 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5670",
    "number": "5670",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "V000134",
        "district": "24",
        "firstName": "Beth",
        "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
        "lastName": "Van Duyne",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Protecting America\u2019s Roads Act",
    "type": "HR",
    "updateDate": "2025-12-10T19:31:54Z",
    "updateDateIncludingText": "2025-12-10T19:31:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-01",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T16:02:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-01T19:44:24Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-09-30T16:02:15Z",
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
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5670ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5670\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 30, 2025 Ms. Van Duyne introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title 49, United States Code, with respect to commercial driver\u2019s license requirements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting America\u2019s Roads Act .\n#### 2. Commercial driver\u2019s license requirements\n##### (a) In general\nSection 31308 of title 49, United States Code, is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (A) by striking and at the end; and\n**(B)**\nby adding at the end the following:\n(C) present valid documentation proving citizenship status, lawful permanent resident status, or a valid work authorization; and (D) present valid documentation of domicile in the State in which the commercial driver\u2019s license is issued; ; and\n**(2)**\nin paragraph (3) by striking and at the end;\n**(3)**\nin paragraph (4)(E) by striking the period and inserting a semicolon; and\n**(4)**\nby adding at the end the following:\n(5) prohibit a State from issuing a commercial driver\u2019s license to an individual who is not domiciled in such State; (6) require States to use the SAVE system for any non-citizen applicant for a commercial driver\u2019s license, maintain documents related to such applicant for not less than 2 years, and deny any applicant if the SAVE system does not confirm lawful presence of such applicant; (7) with respect to any non-citizen applicant for a commercial driver\u2019s license or commercial learner\u2019s permit, the license or learner\u2019s permit shall expire on the earlier of\u2014 (A) the applicant\u2019s I\u201394 date; or (B) 1 year after issuance of such license or permit; (8) require any upgrade, downgrade, renewal, or transfer of a commercial driver\u2019s license or commercial learner\u2019s permit for a non-citizen to be completed in person; and (9) require States to downgrade or revoke any commercial driver\u2019s license or learner\u2019s permit for any non-citizen if eligibility for such license or permit lapses. .\n##### (b) Penalties\nThe Secretary of Transportation shall issue such regulations as are necessary to establish penalties for States that the Secretary finds do not comply with the requirements of section 31308(9) of title 49, United States Code.\n#### 3. Termination of reciprocity for commercial driver\u2019s licenses\nNot later than 6 months after the date of enactment of this Act, the Administrator of the Federal Motor Carrier Safety Administration shall take such actions as are necessary to terminate any existing reciprocity agreements that recognize foreign commercial driver\u2019s licenses in the United States or permit holders of foreign commercial driver\u2019s licenses to operate a commercial motor vehicle in the United States, unless expressly authorized by statute.\n#### 4. Agency cooperation\nNotwithstanding any other provision of law, any agency operating under section 287(g) of the Immigration and Nationality Act ( 8 U.S.C. 1357(g) ) may use the authority of such Agency to identify and address foreign nationals unlawfully operating commercial motor vehicles in the United States and report to the Administrator of the Federal Motor Carrier Safety Administration.\n#### 5. Effective date\nThis Act shall take effect on the date that is 6 months after the date of enactment of this Act.",
      "versionDate": "2025-09-30",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-12-10T19:31:54Z"
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
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5670ih.xml"
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
      "title": "Protecting America\u2019s Roads Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-16T05:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting America\u2019s Roads Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-16T05:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, with respect to commercial driver's license requirements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-16T05:48:31Z"
    }
  ]
}
```
