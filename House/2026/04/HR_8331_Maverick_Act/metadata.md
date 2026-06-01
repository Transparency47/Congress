# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8331?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8331
- Title: Maverick Act
- Congress: 119
- Bill type: HR
- Bill number: 8331
- Origin chamber: House
- Introduced date: 2026-04-16
- Update date: 2026-05-27T08:06:25Z
- Update date including text: 2026-05-27T08:06:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-16: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2026-04-16: Introduced in House

## Actions

- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-16",
    "latestAction": {
      "actionDate": "2026-04-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8331",
    "number": "8331",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "H001098",
        "district": "8",
        "firstName": "Abraham",
        "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
        "lastName": "Hamadeh",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Maverick Act",
    "type": "HR",
    "updateDate": "2026-05-27T08:06:25Z",
    "updateDateIncludingText": "2026-05-27T08:06:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-16",
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
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-16",
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
          "date": "2026-04-16T14:02:25Z",
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
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "AZ"
    },
    {
      "bioguideId": "S001220",
      "district": "5",
      "firstName": "Dale",
      "fullName": "Rep. Strong, Dale W. [R-AL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Strong",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "AL"
    },
    {
      "bioguideId": "S001189",
      "district": "8",
      "firstName": "Austin",
      "fullName": "Rep. Scott, Austin [R-GA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "GA"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "GA"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "VA"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "MI"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "TX"
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
      "sponsorshipDate": "2026-04-16",
      "state": "NC"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "GU"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-05-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8331ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8331\nIN THE HOUSE OF REPRESENTATIVES\nApril 16, 2026 Mr. Hamadeh of Arizona (for himself, Mr. Ciscomani , Mr. Strong , Mr. Austin Scott of Georgia , Mr. McCormick , Mrs. Kiggans of Virginia , Mr. Bergman , Mr. Ellzey , Mr. Davis of North Carolina , and Mr. Moylan ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo authorize the conveyance by the Secretary of the Navy to the U.S. Space and Rocket Center Commission in Huntsville, Alabama, of certain F\u201314D Tomcat aircraft, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Maverick Act of 2026 .\n#### 2. Conveyance of certain F\u201314D Tomcat aircraft to U.S. Space and Rocket Center Commission in Huntsville, Alabama\n##### (a) Authority\nThe Secretary of the Navy may convey, without consideration, to the U.S. Space and Rocket Center Commission in Huntsville, Alabama (in this section referred to as the Commission ), all right, title, and interest of the United States in the following:\n**(1)**\nF\u201314D Tomcat aircraft (Bureau Number 163283).\n**(2)**\nF\u201314D Tomcat aircraft (Bureau Number 164602).\n**(3)**\nF\u201314D Tomcat aircraft (Bureau Number 159437).\n##### (b) Gift\nAny conveyance under subsection (a) shall be made by means of a conditional deed of gift.\n##### (c) Conveyance at no cost to the United States\nAny conveyance under subsection (a) shall be made at no cost to the United States. Any costs associated with such conveyance, costs of determining compliance with terms of the conveyance, and costs of operation and maintenance of the aircraft conveyed shall be borne by the Commission.\n##### (d) Condition of aircraft to be conveyed\n**(1) As-is condition**\nThe Secretary may not be required to repair or alter the condition of any aircraft prior to conveying such aircraft under subsection (a).\n**(2) Manuals; certain spare parts and equipment**\nIf the Secretary elects to convey to the Commission the aircraft under subsection (a), the Secretary shall, prior to such conveyance, provide to the Commission\u2014\n**(A)**\nany operations manuals of the Department of Defense or the Navy specific to the F\u201314D Tomcat aircraft; and\n**(B)**\nsuch excess spare parts or equipment from stocks of the Navy as the Secretary determines necessary to restore such aircraft, or operate or display such aircraft once restored, for a use specified in subsection (e)(2).\n**(3) No obligation to provide other support**\nThe Secretary may not be required to provide any spare part, equipment, manual, or other form of support not specified in paragraph (2)(B) as a result of or in connection with a conveyance authorized under subsection (a).\n**(4) Agreements for restoration and operation**\nThe Secretary may authorize the Commission to enter into one or more agreements with a qualified nonprofit organization for the purpose of restoring the aircraft conveyed under subsection (a) for a use specified in subsection (e)(2).\n##### (e) Terms and conditions\nThe Secretary shall require that any conveyance of aircraft under subsection (a) be carried out by means of an instrument of conveyance that includes, at a minimum, the following:\n**(1)**\nA condition that such aircraft do not possess any capability for use as a platform for launching or releasing munitions or any other combat capability, as determined by the Secretary.\n**(2)**\nA condition that the Commission may only use such aircraft for display or operation in a public static display, an airshow, or a commemorative event to preserve United States naval aviation heritage.\n**(3)**\nA condition that the Commission shall operate and maintain such aircraft in compliance with all applicable limitations and maintenance requirements imposed by the Administrator of the Federal Aviation Administration.\n**(4)**\nA condition that, if the Secretary determines at any time that the Commission has conveyed an ownership interest in, or transferred possession of, such aircraft to any party without the prior approval of the Secretary or has violated a condition specified in paragraph (2) or (3), all right, title, and interest in and to the aircraft, including any repair or alteration of the aircraft, shall revert to the United States, and the United States shall have the right of immediate possession of the aircraft.\n**(5)**\nSuch other terms and conditions as the Secretary considers appropriate to protect the interests of the United States, which may include requirements for demilitarization and indemnification and may restrict further disposition or use.\n##### (f) Clarification of liability\nNotwithstanding any other provision of law, upon the conveyance to the Commission of interests in the aircraft under subsection (a), the United States may not be liable for any death, injury, loss, or damage that results from any use of such aircraft by any person other than the United States.\n##### (g) Applicable law\nThe conveyance of an aircraft under subsection (a), and the use of such aircraft following such conveyance, shall be subject to all applicable Federal and State laws and regulations, including the Arms Export Control Act ( 22 U.S.C. 2751 et seq. ), the Export Control Reform Act of 2018 ( 50 U.S.C. 4801 et seq. ), chapter 37 of title 18, United States Code (commonly referred to as the Espionage Act ), the regulations set forth in subchapter M of chapter I of title 22, Code of Federal Regulations (commonly referred to as the International Traffic in Arms Regulations ), subchapter C of chapter VII of title 15, Code of Federal Regulations (commonly referred to as the Export Administration Regulations ), and chapter V of title 31, Code of Federal Regulations (commonly referred to as the Foreign Assets Control Regulations ).",
      "versionDate": "2026-04-16",
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
        "updateDate": "2026-04-21T04:08:39Z"
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
      "date": "2026-04-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8331ih.xml"
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
      "title": "Maverick Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-18T02:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Maverick Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-18T02:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the conveyance by the Secretary of the Navy to the U.S. Space and Rocket Center Commission in Huntsville, Alabama, of certain F-14D Tomcat aircraft, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-18T02:48:42Z"
    }
  ]
}
```
