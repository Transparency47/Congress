# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7027?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7027
- Title: Restore Veterans’ Compensation Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7027
- Origin chamber: House
- Introduced date: 2026-01-13
- Update date: 2026-05-23T08:07:41Z
- Update date including text: 2026-05-23T08:07:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-13: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-13 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-07 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2026-01-13: Introduced in House

## Actions

- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Introduced in House
- 2026-01-13 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-13 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-07 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-13",
    "latestAction": {
      "actionDate": "2026-01-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7027",
    "number": "7027",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001257",
        "district": "12",
        "firstName": "Gus",
        "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
        "lastName": "Bilirakis",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Restore Veterans\u2019 Compensation Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-23T08:07:41Z",
    "updateDateIncludingText": "2026-05-23T08:07:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-07",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-13",
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
          "date": "2026-01-13T15:02:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-05-07T04:00:00Z",
              "name": "Referred to"
            }
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "systemCode": "hsvr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-01-13T15:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "True",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7027ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7027\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2026 Mr. Bilirakis (for himself and Mr. Levin ) introduced the following bill; which was referred to the Committee on Armed Services , and in addition to the Committee on Veterans' Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title 10, United States Code, to eliminate the recoupment of separation pay, special separation benefits, and voluntary separation incentive payments from members of the Armed Forces who subsequently receive disability compensation under laws administered by the Department of Veterans Affairs and to impose limitations on the authority of the Secretary of Defense to recoup such pay from members who subsequently receive military retired or retainer pay.\n#### 1. Short title\nThis Act may be cited as the Restore Veterans\u2019 Compensation Act of 2026 .\n#### 2. Recoupment of separation pay, special separation benefits, voluntary separation incentive, and voluntary separation pay and benefits from members of the Armed Forces\n##### (a) Separation pay upon involuntary discharge or release from active duty and special separation benefits\n**(1) Elimination of recoupment from members receiving veterans disability compensation**\nParagraph (2) of section 1174(h) of title 10, United States Code, is amended to read as follows:\n(2) (A) A member who has received separation pay under this section, or severance pay or readjustment pay under any other provision of law, based on service in the Armed Forces shall not be deprived, by reason of the receipt of such separation pay, severance pay, or readjustment pay, of any disability compensation to which the member is entitled under the laws administered by the Department of Veterans Affairs. (B) The amount of disability compensation to which a member may be entitled under the laws administered by the Department of Veterans Affairs may not be reduced on account of the receipt of separation pay, severance pay, or readjustment pay. .\n**(2) Recoupment from members receiving retired or retainer pay limited to net amount of separation pay**\nSection 1174(h)(1) of title 10, United States Code, is amended by inserting before the period at the end the following: , less the amount of Federal income tax withheld from the separation pay, severance pay, or readjustment pay (such withholding being at the flat withholding rate for Federal income tax withholding, as in effect pursuant to regulations prescribed under chapter 24 of the Internal Revenue Code of 1986) .\n**(3) Percentage limitations on recoupment from members receiving retired or retainer pay and recoupment process**\nSection 1174(h)(1) of title 10, United States Code, as amended by paragraph (2), is further amended\u2014\n**(A)**\nby inserting (A) after (1) ;\n**(B)**\nby striking shall specify, taking into account the financial ability of the member to pay and avoiding the imposition of undue financial hardship on the member and member\u2019s dependents, and inserting (subject to subparagraph (B)) shall specify ; and\n**(C)**\nby adding at the end the following new subparagraphs:\n(B) The amount deducted under subparagraph (A) from a payment of retired or retainer pay may not exceed 25 percent of the amount of the member\u2019s retired or retainer pay for that month unless the member requests deductions at an accelerated rate. The Secretary of Defense shall consult with the member regarding the repayment rate to be imposed, taking into account the financial ability of the member to pay and avoiding the imposition of an undue hardship on the member and the member\u2019s dependents. (C) The deduction of amounts from the retired or retainer pay of a member under this paragraph may not commence until the date that is 90 days after the date on which the Secretary of Defense notifies the member of the deduction of such amounts under this paragraph. Any notice under this subparagraph shall be designed to provide clear and comprehensive information on the deduction of amounts under this paragraph, including information on the determination of the amount and period of installments under this paragraph. (D) The Secretary of Defense may waive the deduction of amounts from the retired or retainer pay of a member under this paragraph if the Secretary determines that deduction of such amounts would result in a financial hardship for the member. .\n##### (b) Conforming amendments\n**(1) Voluntary separation incentive**\nSection 1175(e) of title 10, United States Code, is amended\u2014\n**(A)**\nin paragraph (3)(A)\u2014\n**(i)**\nby striking the first sentence and inserting the following new sentence: Subsection (h) of section 1174 of this title shall apply to any member who has received the voluntary separation incentive and who later qualifies for retired or retainer pay under this title or for disability compensation under the laws administered by the Department of Veterans Affairs. ; and\n**(ii)**\nin the second sentence, by striking the deduction required under the preceding sentence and inserting the deduction from the member\u2019s retired or retainer pay ; and\n**(B)**\nby striking paragraph (4) and redesignating paragraph (5) as paragraph (4).\n**(2) Voluntary separation pay and benefits**\nSubsection (h) of section 1175a of title 10, United States Code, is amended to read as follows:\n(h) Coordination With Retired or Retainer Pay and Disability Compensation (1) Subsection (h) of section 1174 of this title shall apply to any member who receives voluntary separation pay under this section and who later qualifies for retired or retainer pay under this title or title 14 or for disability compensation under the laws administered by the Department of Veterans Affairs. (2) No deduction shall be made from the disability compensation paid to an eligible disabled uniformed services retiree under section 1413, or to an eligible combat-related disabled uniformed services retiree under section 1413a of this title, who is paid voluntary separation pay under this section. (3) The requirement under this subsection to repay voluntary separation pay following retirement from the Armed Forces does not apply to a member who was eligible to retire at the time the member applied and was accepted for voluntary separation pay and benefits under this section. .\n##### (c) Effective date and application of amendments\nThe amendments made by this section shall take effect on the first day of the first month beginning on or after the date of the enactment of this Act. In the case of deductions to be made from the retired or retainer pay of members of the uniformed services, the amendments shall apply to that month and subsequent months.",
      "versionDate": "2026-01-13",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-04-27T22:13:47Z"
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
      "date": "2026-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7027ih.xml"
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
      "title": "To amend title 10, United States Code, to eliminate the recoupment of separation pay, special separation benefits, and voluntary separation incentive payments from members of the Armed Forces who subsequently receive disability compensation under laws administered by the Department of Veterans Affairs and to impose limitations on the authority of the Secretary of Defense to recoup such pay from members who subsequently receive military retired or retainer pay.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-22T08:01:12Z"
    },
    {
      "title": "Restore Veterans\u2019 Compensation Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-22T07:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Restore Veterans\u2019 Compensation Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-22T07:53:23Z"
    }
  ]
}
```
