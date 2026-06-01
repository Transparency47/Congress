# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8441?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8441
- Title: Military VOTE Act
- Congress: 119
- Bill type: HR
- Bill number: 8441
- Origin chamber: House
- Introduced date: 2026-04-22
- Update date: 2026-04-29T20:30:01Z
- Update date including text: 2026-04-29T20:30:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-22: Introduced in House
- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-22 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-04-22: Introduced in House

## Actions

- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Introduced in House
- 2026-04-22 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-22 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-22",
    "latestAction": {
      "actionDate": "2026-04-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8441",
    "number": "8441",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001117",
        "district": "6",
        "firstName": "Sean",
        "fullName": "Rep. Casten, Sean [D-IL-6]",
        "lastName": "Casten",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Military VOTE Act",
    "type": "HR",
    "updateDate": "2026-04-29T20:30:01Z",
    "updateDateIncludingText": "2026-04-29T20:30:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-22",
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
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-22",
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
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-22",
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
          "date": "2026-04-22T15:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-04-22T15:03:05Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8441ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8441\nIN THE HOUSE OF REPRESENTATIVES\nApril 22, 2026 Mr. Casten introduced the following bill; which was referred to the Committee on House Administration , and in addition to the Committee on Armed Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Uniformed and Overseas Citizens Absentee Voting Act to require States to accept the official post card form prescribed by the Secretary of Defense under such Act when submitted by electronic means, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Military Voters Overseas Technical Enhancement Act or the Military VOTE Act .\n#### 2. Promoting timely and accurate delivery of post card form and absentee ballots\n##### (a) Acceptance of post card form transmitted electronically\n**(1) Requiring acceptance**\nSection 102(a)(4) of the Uniformed and Overseas Citizens Absentee Voting Act ( 52 U.S.C. 20302(a)(4) ) is amended to read as follows:\n(4) use the official post card form prescribed under section 101 for simultaneous voter registration application and absentee ballot application, and accept such post card form when submitted by electronic means (defined as submission by electronic mail or submission through an online portal) or physical means; .\n**(2) Grants to States to assist in meeting requirement**\n**(A) Grants**\nBeginning on the date of the enactment of this Act, the Presidential designee under section 101(a) of the Uniformed and Overseas Citizens Absentee Voting Act ( 52 U.S.C. 20301(a) ) shall make a grant to a State to assist the State in complying with the requirement under section 102(a)(4) of such Act ( 52 U.S.C. 20302(a)(4) ), as amended by paragraph (1), to accept the official post card form prescribed under section 101 of such Act when the form is submitted by electronic mail or through an online portal.\n**(B) Requirements for States**\nThe Presidential designee shall make a grant to a State under this paragraph only if the State provides to the Secretary the following information and assurances:\n**(i)**\nA certification that the State is unable to comply with the requirement described in subparagraph (A).\n**(ii)**\nA description of the State\u2019s existing process for receiving the official post card form described in subparagraph (A).\n**(iii)**\nThe State\u2019s plan to implement the means necessary to comply with such requirement, including a detailed breakdown of the costs the State will incur.\n**(iv)**\nAny further relevant information that the Secretary may request.\n**(C) Authorization of appropriations**\nThere are authorized to be appropriated $40,000,000 to carry out this paragraph.\n**(D) State defined**\nIn this paragraph, the term State means each State, the District of Columbia, the Commonwealth of Puerto Rico, American Samoa, Guam, the United States Virgin Islands, and the Commonwealth of the Northern Mariana Islands.\n##### (b) Electronic transmission of absentee ballots\nSection 102(f)(2) of such Act ( 52 U.S.C. 20302(f)(2) ) is amended to read as follows:\n(2) Transmission if no preference indicated If an absent uniformed services voter or overseas voter does not designate a preference under paragraph (1)(B)\u2014 (A) the State shall transmit the ballot electronically; or (B) if the State lacks sufficient information to transmit the ballot electronically, the State shall transmit the ballot by any delivery method allowable in accordance with applicable State law. .\n##### (c) Effective date\nThis section and the amendments made by this section shall apply with respect to the regularly scheduled general election for Federal office held in November 2026 and each succeeding election for Federal office.\n#### 3. Use of single absentee ballot application for subsequent elections\n##### (a) In general\nSection 104 of the Uniformed and Overseas Citizens Absentee Voting Act ( 52 U.S.C. 20306 ) is amended to read as follows:\n104. Treatment of ballot requests (a) Use of application by absent uniformed services and overseas voters for subsequent elections (1) In general If a State accepts and processes an official post card form (prescribed under section 101) submitted by an absent uniformed services voter or overseas voter for simultaneous voter registration and absentee ballot application (in accordance with section 102(a)(4)) and the voter requests that the application be considered an application for an absentee ballot for each subsequent election for Federal office held in the State, the State shall provide an absentee ballot to the voter\u2014 (A) in the case of a voter who requests the ballot in paper form, for not fewer than the next 2 such subsequent elections; or (B) in the case of a voter who receives the ballot in electronic form, for each such subsequent election. (2) Exceptions Paragraph (1) shall not apply with respect to a voter if\u2014 (A) the voter\u2019s registration is cancelled by the State; (B) the State obtains evidence that the voter is no longer eligible to register to vote or vote as an absent uniformed services voter or overseas voter; or (C) the voter requests that the State no longer provide the voter with an absentee ballot under this subsection. (b) Prohibition of refusal of application on grounds of early submission A State may not refuse to accept or to process, with respect to any election for Federal office, any otherwise valid voter registration application or absentee ballot application (including the post card form prescribed under section 101) submitted by an absent uniformed services voter or overseas voter on the grounds that the voter submitted the application before the first date on which the State otherwise accepts or processes such applications for that election which are submitted by absentee voters who are not members of the uniformed services or overseas citizens. .\n##### (b) Conforming revision to post card form\nSection 101 of such Act ( 52 U.S.C. 20301 ) is amended\u2014\n**(1)**\nin subsection (b)(2), by striking the semicolon and inserting , in accordance with subsection (c); ;\n**(2)**\nby redesignating subsections (b) and (c) as subsections (c) and (d); and\n**(3)**\nby inserting after subsection (a) the following new subsection:\n(c) Use of official post card form for registration for subsequent elections The Presidential designee shall ensure that the official post card form prescribed under subsection (b)(2) enables a voter using the form to request an absentee ballot for subsequent elections for Federal office held in a State, as provided under section 104. .\n##### (c) Effective date\nThe amendments made by this subsection shall apply with respect to voter registration and absentee ballot applications which are submitted to a State or local election official on or after the date of enactment of this Act.\n#### 4. Evaluation of accuracy and timeliness of voter registration information provided to absent uniformed services voters upon transfer to new duty station\nSection 105A of the Uniformed and Overseas Citizens Absentee Voting Act ( 52 U.S.C. 20308 ) is amended\u2014\n**(1)**\nby redesignating subsection (c) as subsection (d); and\n**(2)**\nby inserting after subsection (b) the following new subsection:\n(c) Adequacy of voter registration information provided to members upon transfer to new duty station Not later than one year after the date of the enactment of this subsection, the Presidential designee shall submit to the President and the relevant congressional committees an evaluation of whether the information on voter registration which is included in the change of base packet provided to absent uniformed services voters who are transferred to new duty stations provides timely and accurate information on how such voters may register to vote in elections for Federal office. .\n#### 5. Study and report on feasibility of automatic voter registration\n##### (a) Study\nThe Secretary of Defense shall conduct a study of the feasibility of the creation of a system of automatic voter registration for members of the uniformed services upon enlistment or receiving commission, as well as the creation of a system to automatically update the address of absent members of the uniformed services for voter registration purposes upon any change of address for such member, including an assessment of the feasibility and costs of\u2014\n**(1)**\nusing information already collected as part of the enlistment or commission process for purposes of voter registration, including whether such information is sufficient for States to register an individual to vote, and if not, what other information would need to be collected as part of the enlistment and commission process to enable this process;\n**(2)**\nusing information already collected as part of the enlistment or commission process for purposes of updating voter registration information for existing registrants, including whether such information is sufficient for States to update an existing registration, and if not, what other information would need to be collected as part of the enlistment or commission process to enable this process; and\n**(3)**\nelectronically transmitting such voter registration information to chief State election officials.\n##### (b) Report\nNot later than 180 days after the date of enactment of this Act, the Secretary of Defense shall submit to the Committees on Armed Services of the Senate and House of Representatives, and make publicly available, a report on the study conducted under subsection (a).\n#### 6. No effect on ability to register or revise registration information directly\nNothing in this Act or any amendment made by this Act shall be construed to limit the ability of a member of the Armed Forces to register to vote in elections for Federal office directly with a State election official, or to revise the member\u2019s voter registration information, including the member\u2019s place of residence, directly with a State election official.",
      "versionDate": "2026-04-22",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-04-29T20:30:00Z"
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
      "date": "2026-04-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8441ih.xml"
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
      "title": "Military VOTE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-28T06:08:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Military VOTE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-28T06:08:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Military Voters Overseas Technical Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-28T06:08:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Uniformed and Overseas Citizens Absentee Voting Act to require States to accept the official post card form prescribed by the Secretary of Defense under such Act when submitted by electronic means, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-28T06:03:31Z"
    }
  ]
}
```
