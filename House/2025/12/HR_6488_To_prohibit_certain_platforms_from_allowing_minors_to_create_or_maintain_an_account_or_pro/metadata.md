# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6488?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6488
- Title: RESET Act
- Congress: 119
- Bill type: HR
- Bill number: 6488
- Origin chamber: House
- Introduced date: 2025-12-05
- Update date: 2025-12-19T09:07:12Z
- Update date including text: 2025-12-19T09:07:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-05: Introduced in House
- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-12-05: Introduced in House

## Actions

- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Introduced in House
- 2025-12-05 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-05",
    "latestAction": {
      "actionDate": "2025-12-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6488",
    "number": "6488",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "H001093",
        "district": "9",
        "firstName": "Erin",
        "fullName": "Rep. Houchin, Erin [R-IN-9]",
        "lastName": "Houchin",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "RESET Act",
    "type": "HR",
    "updateDate": "2025-12-19T09:07:12Z",
    "updateDateIncludingText": "2025-12-19T09:07:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-05",
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
      "actionDate": "2025-12-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-05",
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
          "date": "2025-12-05T16:00:20Z",
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
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6488ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6488\nIN THE HOUSE OF REPRESENTATIVES\nDecember 5, 2025 Mrs. Houchin introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo prohibit certain platforms from allowing minors to create or maintain an account or profile on such platforms, and for other proposes.\n#### 1. Short title\nThis Act may be cited as the Reducing Exploitative Social Media Exposure for Teens Act or the RESET Act .\n#### 2. Prohibition on accounts and profiles for minors\n##### (a) Prohibition\n**(1) In general**\nA covered platform may not allow an individual to create or maintain an account or profile on the covered platform if the covered platform knows that the individual is a minor.\n**(2) Termination of existing accounts**\nA covered platform shall\u2014\n**(A)**\nnot later than 60 days after the date of the enactment of this section, identify any account or profile of a user on the covered platform that the covered platform knows is a minor;\n**(B)**\nnot later than 180 days after the date of the enactment of this section, notify any user of an account or profile identified under subparagraph (A) that the covered platform will terminate the account or profile of the user; and\n**(C)**\nnot later than 30 days after the date on which a user is notified pursuant to subparagraph (B), terminate the account or profile of the user.\n**(3) Deletion of the personal data of a minor**\n**(A) In general**\nSubject to subparagraph (B), upon termination of an existing account or profile of a user pursuant to paragraph (2), a covered platform shall immediately delete all personal data collected from the user or submitted by the user to the covered platform.\n**(B) Access to personal data by a minor**\nTo the extent technically feasible and not in violation of any licensing agreement, a covered platform shall allow the user of an existing account or profile that the covered platform has terminated pursuant to paragraph (2), from the date such termination occurs to the date that is 90 days after such date, to request, and shall provide to such user upon such request, a copy of the personal data collected from the user or submitted by the user to the covered platform both\u2014\n**(i)**\nin a manner that is readable and which a reasonable person can understand; and\n**(ii)**\nin a portable, structured, and machine-readable format.\n**(C) Compliance**\nA covered platform shall fulfill a request under subparagraph (B) not later than 45 days after the date on which such request is made to the covered platform.\n##### (b) Enforcement by commission\n**(1) Unfair or deceptive acts or practices**\nA violation of this section shall be treated as a violation of a regulation under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ) regarding unfair or deceptive acts or practices.\n**(2) Powers of commission**\nThe Commission shall enforce this section in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act. Any person who violates this section shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act.\n##### (c) Actions by states\n**(1) In general**\nIn any case in which the attorney general of a State, or an official or agency of a State, has reason to believe that an interest of the residents of such State has been or is threatened or adversely affected by an act or practice in violation of this section, the State, as parens patriae, may bring a civil action on behalf of the residents of the State in an appropriate State court or an appropriate district court of the United States to\u2014\n**(A)**\nenjoin such act or practice;\n**(B)**\nenforce compliance with this section;\n**(C)**\nobtain damages, restitution, or other compensation on behalf of residents of the State; or\n**(D)**\nobtain such other legal and equitable relief as the court may consider to be appropriate.\n**(2) Notice**\nBefore filing an action under this subsection, the attorney general, official, or agency of the State involved shall provide to the Commission a written notice of such action and a copy of the complaint for such action. If the attorney general, official, or agency determines that it is not feasible to provide the notice described in this paragraph before the filing of the action, the attorney general, official, or agency shall provide written notice of the action and a copy of the complaint to the Commission immediately upon the filing of the action.\n**(3) Authority of commission**\n**(A) In general**\nOn receiving notice under paragraph (2) of an action under this subsection, the Commission shall have the right\u2014\n**(i)**\nto intervene in the action;\n**(ii)**\nupon so intervening, to be heard on all matters arising therein; and\n**(iii)**\nto file petitions for appeal.\n**(B) Limitation on state action while federal action is pending**\nIf the Commission or the Attorney General of the United States has instituted a civil action for violation of this Act (referred to in this subparagraph as the Federal action ), no State attorney general, official, or agency may bring an action under this subsection during the pendency of the Federal action against any defendant named in the complaint in the Federal action for any violation of this Act alleged in such complaint.\n**(4) Rule of construction**\nFor purposes of bringing a civil action under this subsection, nothing in this Act shall be construed to prevent an attorney general, official, or agency of a State from exercising the powers conferred on the attorney general, official, or agency by the laws of such State to conduct investigations, administer oaths and affirmations, or compel the attendance of witnesses or the production of documentary and other evidence.\n##### (d) Relationship to other laws\nNo State or political subdivision of a State may prescribe, maintain, or enforce any law, rule, regulation, requirement, standard, or other provision having the force and effect of law, if such law, rule, regulation, requirement, standard, or other provision relates to the provisions of this section.\n##### (e) Effective date\nUnless otherwise specified, this section shall take effect on the date that is 1 year after the date of enactment of this section.\n##### (f) Definitions\nIn this section:\n**(1) Commission**\nThe term Commission means the Federal Trade Commission.\n**(2) Covered platform**\nThe term covered platform has the meaning given that term in section 4 of the TAKE IT DOWN Act ( Public Law 119\u201312 ; 47 U.S.C. 223a note).\n**(3) Know or knows**\nThe term know or knows means to have actual knowledge or to have acted in willful disregard.\n**(4) Minor**\nThe term minor means an individual under the age of 16.\n**(5) Personal data**\nThe term personal data has the meaning given the term personal information in section 1302 of the Children\u2019s Online Privacy Protection Act of 1998 ( 15 U.S.C. 6501 ).\n**(6) User**\nThe term user means, with respect to a covered platform, an individual who creates or maintains an account or profile on the covered platform.",
      "versionDate": "2025-12-05",
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
        "name": "Commerce",
        "updateDate": "2025-12-10T21:36:02Z"
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
      "date": "2025-12-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6488ih.xml"
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
      "title": "RESET Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-09T10:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "RESET Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-09T10:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Reducing Exploitative Social Media Exposure for Teens Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-09T10:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit certain platforms from allowing minors to create or maintain an account or profile on such platforms, and for other proposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-09T10:18:15Z"
    }
  ]
}
```
