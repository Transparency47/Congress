# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7228?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7228
- Title: Maintain Access to Vital Social Security Services Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7228
- Origin chamber: House
- Introduced date: 2026-01-22
- Update date: 2026-02-12T15:14:13Z
- Update date including text: 2026-02-12T15:14:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-22: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-01-22: Introduced in House

## Actions

- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-22",
    "latestAction": {
      "actionDate": "2026-01-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7228",
    "number": "7228",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "M001160",
        "district": "4",
        "firstName": "Gwen",
        "fullName": "Rep. Moore, Gwen [D-WI-4]",
        "lastName": "Moore",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "Maintain Access to Vital Social Security Services Act of 2026",
    "type": "HR",
    "updateDate": "2026-02-12T15:14:13Z",
    "updateDateIncludingText": "2026-02-12T15:14:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-22",
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
      "actionDate": "2026-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-22",
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
          "date": "2026-01-22T14:05:15Z",
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
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "DC"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7228ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7228\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2026 Ms. Moore of Wisconsin (for herself, Ms. Johnson of Texas , and Ms. Norton ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend title VII of the Social Security Act to improve the Social Security Administration\u2019s procedures to close or reduce access to field offices, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Maintain Access to Vital Social Security Services Act of 2026 .\n#### 2. Field offices\n##### (a) In general\nTitle VII of the Social Security Act ( 42 U.S.C. 701 et seq. ) is amended by adding at the end the following:\n714. Field offices (a) In general (1) Number of field offices and personnel The Commissioner shall operate a sufficient number of field offices and employ an sufficient number of personnel at each field office to\u2014 (A) provide comprehensive, convenient, and accessible services to the public; (B) meet current and projected workloads, including consideration of anticipated workload or population changes identified through a service area review; and (C) maintain posted public operating hours to the maximum extent possible and minimize wait-times at each field office, including for those without appointments. (2) Minimum requirement Notwithstanding paragraph (1), the Commissioner take such actions as are necessary to ensure that the number of personnel assigned to field offices is not less than the number so assigned on January 1, 2025. (b) Procedure To close or reduce access to a field office (1) In general (A) Requirement to follow procedure The Commissioner may not take any action described in subparagraph (B) with respect to a field office except in accordance with this subsection. (B) Covered actions The actions described in this subparagraph with respect to a field office are the following: (i) Permanently closing a field office, including by ending or electing not to renew a lease for a field office. (ii) Ending, or electing not to renew, a lease for any field office. (iii) Consolidating the field office with one or more other field offices. (iv) Any other action that would impose a new limitation on public access or reduce in-person services at a field office. (C) Public health emergency exception This subsection shall not apply for the duration of any public health emergency under section 319(a) of the Public Health Service Act ( 42 U.S.C. 247d(a) ). (2) Notification of anticipated action (A) In general Not later than 180 days before the date on which the Commissioner intends any action described in paragraph (1)(B) with respect to a field office to take effect, the Commissioner shall promulgate a public notification of such action that includes the following information: (i) An identification of the field office. (ii) The date on which such action is intended to take effect. (iii) The reasons for taking such action, including, if applicable, the reasons for rejecting any available alternative actions such as relocation of the field office and the role, if any, played by the General Services Administration in contributing to such decision. (iv) The date, time, and location of the public hearings to be held pursuant to paragraph (3). (v) Any alternative means of receiving assistance related to social security which may be used by individuals served by the field office. (vi) Contact information, including by phone and internet, by which individuals may inquire for more information related to such action. In promulgating a notification under this paragraph, the Commissioner shall post such notification at the affected field office and other nearby field offices, mail such notification to residents in the area served by such field offices, publish such notification in newspapers printed in such area, or take such other actions as the Commissioner determines to be necessary. (B) Congressional notification As soon as practicable and not later than 180 days before the date on which the Commissioner intends any action described in paragraph (1)(B) with respect to a field office to take effect, the Commissioner shall provide written notification to each member of Congress and Senator whose constituents are served by such field office. (C) Local Government notification and involvement As soon as practicable and not later than 180 days before the date on which the Commissioner intends any action described in paragraph (1)(B) with respect to a field office to take effect, the Commissioner shall provide written notification to any unit of local government within the service area of such field office and provide the opportunity for local governments to propose alternatives for such action. (3) Opportunity for public comment (A) Public hearing Not earlier than 30 days and not later than 120 days after a notification is published under paragraph (2)(A) with respect to any action described in paragraph (1)(B) with respect to a field office, the Commissioner shall hold not fewer than two public hearings in the geographic area served by the field office, at which the Commissioner shall\u2014 (i) present the reasons for taking such action, including the criteria used to select the field office for such action and, if applicable, the reasons for rejecting any available alternative actions such as relocation of the field office within the area served; (ii) describe the Social Security Administration\u2019s plan to mitigate disruption in service for the community served by the field office, including any special needs of the community and any anticipated impact on vulnerable populations such as the elderly, individuals with disabilities, and those with language or mobility challenges; and (iii) provide an opportunity for public comment, including an opportunity to recommend alternatives to such action. (B) Submission of written comments The Commissioner shall accept written comments from the public relating to such action during the period described in subparagraph (A), which shall be posted on the website of the Social Security Administration. (4) Public report on hearing Not later than 15 days before the date on which any action described in paragraph (1)(B) with respect to a field office takes effect, the Commissioner shall prominently publish on the website of the Social Security Administration a written report that describes the action the Commissioner intends to take with respect to the field office after giving full consideration to, any alternatives proposed by local governments pursuant to paragraph (2)(c) and any public comments received during the period described in paragraph (3)(A). Such report shall include a response by the Commissioner to each unique written comment received during such period. The Commissioner shall submit a copy of such report to each member of Congress identified pursuant to paragraph (2)(B), the Committees on Appropriations of the House of Representatives and the Senate, the Committee on Ways and Means of the House of Representatives, and the Committee on Finance of the Senate. (5) Approval by Inspector General of the Social Security Administration No action described in paragraph (1)(B) may go into effect until the Inspector General of the Social Security Administration has reviewed any health and safety claims made by the Commissioner with respect to such action and has determined that the Commissioner substantially and procedurally complied with all applicable laws, regulations, and guidelines with respect to such action. .\n##### (b) Moratorium\nThe Commissioner may not take any action described in section 714(b)(1)(B) of the Social Security Act ( 42 U.S.C. 914(b)(1)(B) ) with respect to a field office until the date that is 30 days after the date on which the Inspector General of the Social Security Administration provides a written determination that the amendments made by subsection (a) have been fully implemented by the Social Security Administration, except that in the case of such an action related to health and safety reviewed by the Inspector General, such action may take effect for a period not to exceed 30 days unless the Commissioner provides public notice explaining the need to extend such period.\n#### 3. Recommendations of Social Security Advisory Board\nSection 703(b)(4) of title VII of the Social Security Act ( 42 U.S.C. 903(b)(4) ) is amended by striking public and inserting public, taking into account the impact of closing field offices on the quality of service to individuals with disabilities or language barriers or other vulnerable populations .\n#### 4. Report to Congress\nNot later than 180 days after the date of the enactment of this Act, the Commissioner shall submit to the Committee on Ways and Means of the House of Representatives and the Committee on Finance of the Senate a report that\u2014\n**(1)**\nincludes a list of all field offices closed during the 5-year period ending on the date of enactment of this Act, the reason for each such closure, and any impacts of each such closure on wait-times and staffing at nearby affected field offices;\n**(2)**\ndescribes the role played by the Government Services Administration (GSA) in each of the field office closings in identifying any available alternative actions such as relocation of the field office, including a detailed description of\u2014\n**(A)**\nthe number of alternative locations identified by the GSA during each closure procedure;\n**(B)**\nwhether the GSA sought input (and the means by which that input was solicited) on alternative locations from State or local public officials or the public in the affected service area (including how many days, weeks, months, or years prior to the closing the GSA sought such input) and the most common cited reasons for not finding suitable alternative locations prior to closing a field office; and\n**(C)**\nany recommendations for how to improve the transparency and adequacy of the process for soliciting and determining the appropriateness of alternative space for relocation prior to closing a field office; and\n**(3)**\ndescribes a plan\u2014\n**(A)**\nto ensure that field offices are receiving sufficient resources to maintain at least the level of constituent services provided in the previous fiscal year; and\n**(B)**\nto adequately address the number of individuals projected to use field offices during the 10-year period beginning on the date of enactment of this Act.",
      "versionDate": "2026-01-22",
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
        "name": "Social Welfare",
        "updateDate": "2026-02-12T15:14:13Z"
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
      "date": "2026-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7228ih.xml"
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
      "title": "Maintain Access to Vital Social Security Services Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-06T03:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Maintain Access to Vital Social Security Services Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-06T03:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title VII of the Social Security Act to improve the Social Security Administration's procedures to close or reduce access to field offices, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-06T03:18:18Z"
    }
  ]
}
```
