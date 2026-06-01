# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8056?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8056
- Title: Military Financial Literacy Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8056
- Origin chamber: House
- Introduced date: 2026-03-24
- Update date: 2026-05-21T08:08:38Z
- Update date including text: 2026-05-21T08:08:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-24: Introduced in House
- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2026-03-24: Introduced in House

## Actions

- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Introduced in House
- 2026-03-24 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-24",
    "latestAction": {
      "actionDate": "2026-03-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8056",
    "number": "8056",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001237",
        "district": "8",
        "firstName": "Kristen",
        "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
        "lastName": "McDonald Rivet",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Military Financial Literacy Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:38Z",
    "updateDateIncludingText": "2026-05-21T08:08:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-24",
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
      "actionDate": "2026-03-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-24",
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
          "date": "2026-03-24T16:03:35Z",
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
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "NC"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "PA"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "CO"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "RI"
    },
    {
      "bioguideId": "B001323",
      "district": "0",
      "firstName": "Nicholas",
      "fullName": "Rep. Begich, Nicholas J. [R-AK-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Begich",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "AK"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "NC"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "CO"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "CA"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
      "state": "OH"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8056ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8056\nIN THE HOUSE OF REPRESENTATIVES\nMarch 24, 2026 Ms. McDonald Rivet (for herself and Mr. Harrigan ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo expand credentialed, personalized financial and housing counseling to members of the Armed Forces serving on active duty or transitioning from service, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Military Financial Literacy Act of 2026 .\n#### 2. Expansion of personalized financial and housing counseling for members of the Armed Forces\n##### (a) In general\nSection 992 of title 10, United States Code, is amended\u2014\n**(1)**\nin subsection (a)(1)\u2014\n**(A)**\nby redesignating subparagraphs (D) and (E) as subparagraphs (E) and (F), respectively; and\n**(B)**\nby inserting after subparagraph (C) the following new subparagraph:\n(D) practices relating to financial management, home buying and selling, renting during changing permanent station, rental planning, home loans available through the programs of the Department of Veterans Affairs, and other financial services that are routinely offered to private sector home loans; ;\n**(2)**\nby redesignating subsection (d) through (f) as subsections (e) through (g), respectively; and\n**(3)**\nby inserting after subsection (c) the following new subsection:\n(d) Individualized financial and housing counseling (1) Not later than one year after the date of the enactment of this subsection, the Secretary of Defense shall establish a program in accordance with this section and Department of Defense Instruction 1322.34, or any successor guidance, to provide one-on-one counseling tailored to the needs of each member of the armed forces on the following topics: (A) Credit management. (B) Budgeting. (C) Anti-predatory lending practices. (D) Changes of permanent station and rental planning. (E) Home loans available through the programs of the Department of Veterans Affairs. (F) Protections under the Servicemembers Civil Relief Act ( 50 U.S.C. 3901 et seq. ) and section 987 of this title. (2) For the purposes of carrying out paragraph (1), the Secretary shall seek to enter an agreement with a counseling service organization that\u2014 (A) is a HUD-approved counseling agency (as defined in section 106(h) of the House and Urban Development Act of 1968 ( 12 U.S.C. 1701x(h) )); (B) is organized as a tax-exempt entity under section 501(c)(19) of the Internal Revenue Code of 1986, defined by the Internal Revenue Service as a Veteran Service Organization serving the military-connected community; (C) has expertise in financial literacy, housing stability, and home loan benefits for veterans; and (D) is capable of developing, administering, maintaining, and providing specialized training and certification for HUD-Certified Housing Counselors serving members of the armed forces, veterans, and their families. .\n##### (b) Regulations\nThe Secretary of Defense may prescribe such regulations as are necessary to carry out the amendments made by subsection (a).\n##### (c) Report\nNot later than 2 years after the date on which the services required under subsection (d) of section section 992 of title 10, United States Code, as added by subsection (a), are established, the Secretary of Defense shall submit to the Committees on Armed Services of the Senate and the House of Representatives a report on the implementation of such services, including\u2014\n**(1)**\nthe number of members of the Armed Forces who received counseling for housing stability, home loan benefits for veterans, or rental planning;\n**(2)**\nthe rate of completion of the counseling services offered under the pilot program; and\n**(3)**\nindicators of financial stress and housing instability for members of the Armed Forces participating in the pilot program and any metrics for mitigating risks to the members participating.",
      "versionDate": "2026-03-24",
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
        "updateDate": "2026-04-09T20:37:05Z"
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
      "date": "2026-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8056ih.xml"
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
      "title": "Military Financial Literacy Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-07T05:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Military Financial Literacy Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-07T05:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To expand credentialed, personalized financial and housing counseling to members of the Armed Forces serving on active duty or transitioning from service, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-07T05:48:28Z"
    }
  ]
}
```
