# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7234?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7234
- Title: Human Trafficking Awareness Training Recognition Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7234
- Origin chamber: House
- Introduced date: 2026-01-22
- Update date: 2026-05-16T08:07:32Z
- Update date including text: 2026-05-16T08:07:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-22: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-22 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-23 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- Latest action: 2026-01-22: Introduced in House

## Actions

- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-22 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-23 - Committee: Referred to the Subcommittee on Border Security and Enforcement.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7234",
    "number": "7234",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "V000129",
        "district": "22",
        "firstName": "David",
        "fullName": "Rep. Valadao, David G. [R-CA-22]",
        "lastName": "Valadao",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Human Trafficking Awareness Training Recognition Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:32Z",
    "updateDateIncludingText": "2026-05-16T08:07:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-23",
      "committees": {
        "item": {
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Border Security and Enforcement.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-22",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-22",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
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
          "date": "2026-01-22T14:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-23T05:00:00Z",
              "name": "Referred to"
            }
          },
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "systemCode": "hshm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-01-22T14:00:10Z",
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
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "LA"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "NC"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7234ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7234\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2026 Mr. Valadao (for himself, Mr. Carter of Louisiana , and Mr. Davis of North Carolina ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Homeland Security , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo direct the Secretary of Homeland Security to establish a Blue Campaign Certification Program to encourage employers in covered industries to encourage employees to complete training to recognize and respond to suspected human trafficking, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Human Trafficking Awareness Training Recognition Act of 2026 .\n#### 2. Award\nThe Homeland Security Act of 2002 ( 6 U.S.C. 231 et seq. ) is amended by inserting after section 434 the following:\n434A. Blue Campaign Certification Program (a) Program established Not later than one year after the date of the enactment of this section, the Secretary of Homeland Security shall establish a Blue Campaign Certification Program (in this section referred to as the Program ) to encourage efforts by employers in covered industries to encourage employees to complete training to recognize and respond to suspected human trafficking. The Secretary shall provide a certificate of completion to eligible employers. (b) Application process (1) Solicitation of applications During each year in which the Secretary provides a certificate of completion, the Secretary shall solicit applications, beginning not later than January 31 and ending not earlier than April 30, from employers to consider whether such employers should receive such certificate. (2) Review of applications The Secretary, in consultation with the Director of Homeland Security Investigations, shall review each application received in a year. (3) Contents of applications The Secretary shall require each employer who submits an application to provide in such application\u2014 (A) information about the training to recognize and respond to suspected human trafficking that such employer provided to the employees of such employer; and (B) any other information the Secretary determines appropriate. (c) Recognition of recipients (1) Issuance of awards The Secretary shall provide a certificate of completion to each employer whom the Secretary determines is eligible. The certificate of completion shall state that the recipient may display such certificate for a 1-year period beginning on the date on which such certificate is provided. (2) Notice in Federal Register The Secretary shall recognize each such recipient through publication in the Federal Register. (d) Prohibited display It is prohibited for any employer to publicly display a Blue Campaign Certification of Completion\u2014 (1) for the purpose of conveying, or in a manner reasonably calculated to convey, a false impression that the employer completed the Blue Campaign Certification Program, if such employer did not complete such Program; or (2) for the purpose of conveying, or in a manner reasonably calculated to convey, a false impression that the employer received a certificate of completion through the Blue Campaign Certification Program for a year for which such employer did not receive such certificate. (e) Reports During each year beginning not later than two years after the date of the enactment of this section, the Secretary shall submit to the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate, a report on the Program, including\u2014 (1) the number of employers who submitted an application for Blue Campaign Certification in the prior year; (2) the fees collected under subsection (f) from such employers, and any changes in fees to be proposed in the present year; (3) the number of Blue Campaign Certifications of Completion provided in the prior year, including the name of each employer to whom a Blue Campaign Certification of Completion was awarded; (4) the cost of administering the Program in the prior year; and (5) any other matter the Secretary determines appropriate. (f) Authorization for application fees The Secretary is authorized to establish a reasonable fee to be imposed on employers submitting applications for a Blue Campaign Certification of Completion to cover the cost of carrying out the Program. (g) Definitions In this section: (1) Covered industry The term covered industry means any industry that the Secretary has determined\u2014 (A) has a relatively high prevalence of human trafficking; and (B) that human trafficking awareness training could have a significant impact. (2) Employer The term employer has the meaning given such term in section 3 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 203 ), except that such term does not include a public agency (as defined in such section 3). (3) Human trafficking The term human trafficking has the meaning given the term severe forms of trafficking in person in section 103 of the Trafficking Victims Protection Act of 2000 ( 22 U.S.C. 7102 ). (4) Secretary of Homeland Security The term Secretary of Homeland Security means the Secretary of Homeland Security, acting through the Director of the Blue Campaign. (5) Training The term training means the training to recognize and respond to suspected human trafficking. .\n#### 3. Blue Campaign\nSection 434(e) of the Homeland Security Act of 2002 ( 6 U.S.C. 242(e) ) is amended\u2014\n**(1)**\nin paragraph (7), by striking and at the end;\n**(2)**\nby redesignating paragraph (8) as paragraph (9); and\n**(3)**\nby inserting after paragraph (7) the following:\n(8) increased coordination with experts from the private sector, academic institutions, and other covered industries (as such term is defined in section 434A). .",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-02-12T15:27:53Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7234ih.xml"
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
      "title": "Human Trafficking Awareness Training Recognition Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-06T03:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Human Trafficking Awareness Training Recognition Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-06T03:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Homeland Security to establish a Blue Campaign Certification Program to encourage employers in covered industries to encourage employees to complete training to recognize and respond to suspected human trafficking, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-06T03:18:31Z"
    }
  ]
}
```
