# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8253?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8253
- Title: BITMAP Authorization Act
- Congress: 119
- Bill type: HR
- Bill number: 8253
- Origin chamber: House
- Introduced date: 2026-04-13
- Update date: 2026-05-16T08:07:29Z
- Update date including text: 2026-05-16T08:07:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-13: Introduced in House
- 2026-04-13 - IntroReferral: Introduced in House
- 2026-04-13 - IntroReferral: Introduced in House
- 2026-04-13 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-04-14 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- Latest action: 2026-04-13: Introduced in House

## Actions

- 2026-04-13 - IntroReferral: Introduced in House
- 2026-04-13 - IntroReferral: Introduced in House
- 2026-04-13 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2026-04-14 - Committee: Referred to the Subcommittee on Border Security and Enforcement.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-13",
    "latestAction": {
      "actionDate": "2026-04-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8253",
    "number": "8253",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "M001157",
        "district": "10",
        "firstName": "Michael",
        "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
        "lastName": "McCaul",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "BITMAP Authorization Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:29Z",
    "updateDateIncludingText": "2026-05-16T08:07:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-14",
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
      "actionDate": "2026-04-13",
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
      "text": "Referred to the House Committee on Homeland Security.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-13",
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
          "date": "2026-04-13T18:31:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-04-14T19:45:41Z",
              "name": "Referred to"
            }
          },
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "systemCode": "hshm00",
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
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "TX"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "FL"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8253ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8253\nIN THE HOUSE OF REPRESENTATIVES\nApril 13, 2026 Mr. McCaul (for himself and Mr. Cuellar ) introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo amend the Homeland Security Act of 2002 to establish in the Department of Homeland Security the Biometric Identification Transnational Migration Alert Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Biometric Identification Transnational Migration Alert Program Authorization Act or the BITMAP Authorization Act .\n#### 2. Biometric identification transnational migration alert program\n##### (a) In general\nSubtitle D of title IV of the Homeland Security Act of 2002 ( 6 U.S.C. 251 et seq. ) is amended by adding at the end the following new section:\n448. Biometric identification transnational migration alert program (a) Establishment In addition to the Secretary\u2019s existing information sharing authorities provided under this title, the Immigration and Nationality Act (INA), or any other immigration law, there is established in the Department a program to be known as the Biometric Identification Transnational Migration Alert Program (referred to in this section as BITMAP ) to address and reduce national security, border security, and terrorist threats before such threats reach the international border of the United States. (b) Duties In carrying out BITMAP operations, the Secretary, acting through the Director of U.S. Immigration and Customs Enforcement, shall\u2014 (1) coordinate, in consultation with the Secretary of State, and the Director of National Intelligence, with appropriate representatives of foreign governments, and the heads of other Federal agencies, as appropriate, to facilitate the voluntary sharing of biometric and biographic information collected from foreign nationals for the purpose of identifying and screening such nationals to identify those nationals who may pose a terrorist threat or a threat to national security or border security; (2) provide capabilities, including training and equipment, to partner countries to voluntarily collect biometric and biographic identification data from individuals to identify, prevent, detect, and interdict high risk individuals identified as national security, border security, or terrorist threats who may attempt to enter the United States utilizing illicit pathways; (3) provide capabilities, including training and equipment, to partner countries to compare foreign data against appropriate United States national security, border security, terrorism, immigration, and counter-terrorism data, including\u2014 (A) the Department\u2019s Automated Biometric Identification System (commonly known as IDENT ), or successor database; (B) the Federal Bureau of Investigation\u2019s Terrorist Screening Database, or successor database; (C) the Federal Bureau of Investigation\u2019s Next Generation Identification database, or successor database; (D) the Department of Defense Automated Biometric Identification System (commonly known as ABIS ), or successor database; and (E) any other database, notice, or means that the Secretary, in consultation with the heads of other Federal departments and agencies responsible for such databases, notices, or means, designates; (4) provide partner countries with training, guidance, and best practices recommendations regarding the enrollment of individuals in BITMAP; and (5) ensure biometric and biographic identification data collected pursuant to BITMAP are incorporated into appropriate United States Government databases, in compliance with the Privacy Act of 1974, 5 U.S.C. 552a . (c) Collaboration The Secretary shall ensure that BITMAP operations include participation from relevant components of the Department, and request participation from other Federal agencies, as appropriate. Notwithstanding any other provision of law, the Secretary may enter into agreements related to such participation on a reimbursable or non-reimbursable basis, as appropriate. (d) Agreements Before carrying out BITMAP operations in a foreign country that, as of the date of the enactment of this section, was not a partner country described in this section, the Secretary, in consultation with the Secretary of State, shall enter into agreement or arrangement with the government of such country that sets forth program goals for such country, includes training, guidance, and best practices recommendations regarding the enrollment of individuals in BITMAP, and outlines such operations in such country, including related departmental operations. Such country shall be a partner country described in this section pursuant to and for purposes of such agreement or arrangement. (e) Notification to congress Not later than 60 days after an agreement or arrangement with the government of a foreign country to carry out BITMAP operations in such foreign country enters into force, the Secretary shall provide the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate with a copy of such agreement or arrangement to establish such operations, including the following: (1) The identification of the foreign country with which the Secretary enters into such an agreement or arrangement. (2) Goals for BITMAP operations in the foreign country. (f) Captured information of united states citizens The Secretary shall ensure that any biometric or biographic identification data of United States citizens that is captured by BITMAP operations is expunged from all databases to which such data was uploaded, unless such data is retained for specific law enforcement or intelligence purposes. (g) Sunset This section shall terminate on the date that is six years after the date of the enactment of this section. .\n##### (b) Report\nNot later than 180 days after the date on which the Biometric Identification Transnational Migration Alert Program (BITMAP) is established under section 448 of the Homeland Security Act of 2002 (as added by subsection (a) of this section) and annually thereafter for the following five years, the Secretary of Homeland Security shall submit to the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate a report that\u2014\n**(1)**\noutlines the strategic goals and operational plans for BITMAP;\n**(2)**\noutlines key efforts and the progress made with each partner country;\n**(3)**\nprovides a description of the agreement or arrangement with the government of each such partner country, if practicable;\n**(4)**\nprovides budget information related to expenditures in support of BITMAP, including the source of funding and anticipated expenditures;\n**(5)**\nsets forth Department of Homeland Security personnel, equipment, and infrastructure support to be used by BITMAP, disaggregated by country and number;\n**(6)**\nincludes the number of individuals each partner country enrolled into BITMAP during the reporting period, disaggregated by key categories, as determined by U.S. Immigration and Customs Enforcement;\n**(7)**\nincludes the training, guidance, and best practices recommendations provided pursuant to subsection (b)(4) of such section 448;\n**(8)**\nincludes a review of the redress process for BITMAP; and\n**(9)**\ndetails the effectiveness of BITMAP operations in enhancing national security, border security, and counterterrorism operations.\n##### (c) Briefings\nNot later than 30 days after each report is submitted pursuant to subsection (b), the Secretary of Homeland Security shall brief the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Homeland Security of the House of Representatives regarding\u2014\n**(1)**\nindividuals enrolled in BITMAP who have been apprehended at the United States border or in the interior of the United States; and\n**(2)**\nasylum claims that were submitted by individuals who are enrolled in BITMAP.\n##### (d) GAO audit\nNot later than six months after the date of the enactment of this Act and every three years thereafter, the Comptroller General of the United States shall\u2014\n**(1)**\nconduct an audit that analyzes the effectiveness of BITMAP operations; and\n**(2)**\nsubmit to the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Homeland Security of the House of Representatives a report containing the results of such audit.\n##### (e) Clerical amendment\nThe table of contents in section 1(b) of the Homeland Security Act of 2002 is amended by inserting after the item relating to section 447 the following new item:\nSec. 448. Biometric Identification Transnational Migration Alert Program. .",
      "versionDate": "2026-04-13",
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
        "updateDate": "2026-04-22T19:07:31Z"
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
      "date": "2026-04-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8253ih.xml"
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
      "title": "BITMAP Authorization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-21T09:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BITMAP Authorization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-21T09:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Biometric Identification Transnational Migration Alert Program Authorization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-21T09:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Homeland Security Act of 2002 to establish in the Department of Homeland Security the Biometric Identification Transnational Migration Alert Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-21T09:19:02Z"
    }
  ]
}
```
