# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1690?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1690
- Title: SCREEN Act
- Congress: 119
- Bill type: HR
- Bill number: 1690
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2025-05-08T16:21:08Z
- Update date including text: 2025-05-08T16:21:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-27 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-27 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1690",
    "number": "1690",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "G000590",
        "district": "7",
        "firstName": "Mark",
        "fullName": "Rep. Green, Mark E. [R-TN-7]",
        "lastName": "Green",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "SCREEN Act",
    "type": "HR",
    "updateDate": "2025-05-08T16:21:08Z",
    "updateDateIncludingText": "2025-05-08T16:21:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:12:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-27T14:12:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "GU"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "FL"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1690ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1690\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Green of Tennessee (for himself, Mr. Moylan , and Ms. Salazar ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on Oversight and Government Reform , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo limit the use of funds for the production of films using assets of the Department of State under certain circumstances, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stopping Communist Regimes from Engaging in Edits Now Act or the SCREEN Act .\n#### 2. Limitation on use of funds for production of films and prohibition on use of such funds for films subject to conditions on content or altered for screening in the People's Republic of China or at the request of the Chinese Communist Party\n##### (a) Limitation on use of funds\nThe Secretary of State may only authorize the provision of technical support or access to an asset controlled by or related to the Department of State to enter into a contract relating to the production or funding of a film by a United States company if the United States company, as a condition of receiving the support or access\u2014\n**(1)**\nprovides to the Secretary a list of all films produced or funded by that company the content of which has been submitted, during the shorter of the preceding 10-year period or the period beginning on the date of the enactment of this Act, to an official of the Government of the People\u2019s Republic of China or the Chinese Communist Party (CCP) for evaluation with respect to screening the film in the People\u2019s Republic of China (PRC);\n**(2)**\nincludes, with respect to each such film\u2014\n**(A)**\nthe title of the film; and\n**(B)**\nthe date on which such submission occurred;\n**(3)**\nenters into a written agreement with the Secretary not to alter the content of the film in response to, or in anticipation of, a request by an official of the Government of the PRC or the CCP; and\n**(4)**\nsubmits such agreement to the Secretary.\n##### (b) Prohibition with respect to films subject to conditions on content or altered for screening in the people\u2019s republic of china\nNotwithstanding subsection (a), the President may not authorize the provision of technical support or access to any asset controlled by the Federal Government for, or authorize the head of a Federal agency to enter into any contract relating to, the production or funding of a film by a United States company if\u2014\n**(1)**\nthe film is co-produced by an entity located in the PRC that is subject to conditions on content imposed by an official of the Government of the PRC or the CCP; or\n**(2)**\nwith respect to the most recent report submitted under subsection (c), the United States company is listed in the report pursuant to subparagraph (C) or (D) of paragraph (2) of that subsection.\n##### (c) Report to congress\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter, the Secretary of State shall submit to the appropriate committees of Congress a report on films disclosed under subsection (a) that are associated with a United States company that has received technical support or access to an asset controlled by the Department of State for, or has entered into a contract with the Federal Government relating to, the production or funding of a film.\n**(2) Elements**\nThe report required by paragraph (1) shall include the following:\n**(A)**\nA description of each film listed pursuant to the requirement under subsection (a)(1), the content of which was submitted, during the shorter of the preceding 10-year period or the period beginning on the date of the enactment of this Act, by a United States company to an official of the Government of the PRC or the CCP for evaluation with respect to screening the film in the PRC, including\u2014\n**(i)**\nthe United States company that submitted the contents of the film;\n**(ii)**\nthe title of the film; and\n**(iii)**\nthe date on which such submission occurred.\n**(B)**\nA description of each film with respect to which a United States company entered into a written agreement with the Department of State, providing the support or access, pursuant to the requirement under subsection (a)(2) not to alter the content of the film in response to, or in anticipation of, a request by an official of the Government of the PRC or the CCP, during the shorter of the preceding 10-year period or the period beginning on the date of the enactment of this Act, including\u2014\n**(i)**\nthe United States company that entered into the agreement; and\n**(ii)**\nthe title of the film.\n**(C)**\nThe title of any film described pursuant to subparagraph (A), and the corresponding United States company described pursuant to clause (i) of that subparagraph\u2014\n**(i)**\nthat was submitted to an official of the Government of the PRC or the CCP during the preceding 3-year period; and\n**(ii)**\nfor which the Secretary assesses that the content was altered in response to, or in anticipation of, a request by an official of the Government of the PRC or the CCP.\n**(D)**\nThe title of any film that is described in both subparagraph (A) and subparagraph (B), and the corresponding one or more United States companies described in clause (i) of each such subparagraph\u2014\n**(i)**\nthat was submitted to an official of the Government of the PRC or the CCP during the preceding 10-year period; and\n**(ii)**\nfor which the Secretary assesses that the content was altered in response to, or in anticipation of, a request by an official of the Government of the PRC or the CCP.\n##### (d) Definitions\nIn this section:\n**(1) Appropriate committees of congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Foreign Relations of the Senate; and\n**(B)**\nthe Committee on Foreign Affairs of the House of Representatives.\n**(2) Content**\nThe term content means any description of a film, including the script.\n**(3) United states company**\nThe term United States company means a private entity incorporated under the laws of the United States or any jurisdiction within the United States.",
      "versionDate": "2025-02-27",
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
        "name": "International Affairs",
        "updateDate": "2025-05-08T16:21:08Z"
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
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1690ih.xml"
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
      "title": "SCREEN Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-19T09:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SCREEN Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T09:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stopping Communist Regimes from Engaging in Edits Now Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T09:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To limit the use of funds for the production of films using assets of the Department of State under certain circumstances, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-19T09:48:29Z"
    }
  ]
}
```
