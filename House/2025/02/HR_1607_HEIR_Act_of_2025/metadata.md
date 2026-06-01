# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1607?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1607
- Title: HEIR Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1607
- Origin chamber: House
- Introduced date: 2025-02-26
- Update date: 2026-05-20T08:08:02Z
- Update date including text: 2026-05-20T08:08:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-26: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-02-26: Introduced in House

## Actions

- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1607",
    "number": "1607",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "F000468",
        "district": "7",
        "firstName": "Lizzie",
        "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
        "lastName": "Fletcher",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "HEIR Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:02Z",
    "updateDateIncludingText": "2026-05-20T08:08:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-26",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-26",
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
          "date": "2025-02-26T15:06:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MO"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "GA"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MS"
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
      "sponsorshipDate": "2025-02-26",
      "state": "DC"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "FL"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "MI"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "OH"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "TX"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "LA"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "AL"
    },
    {
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1607ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1607\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 26, 2025 Mrs. Fletcher (for herself, Mr. Cleaver , Ms. Williams of Georgia , Mr. Thompson of Mississippi , Ms. Norton , Mr. Soto , Ms. Tlaib , Mrs. Beatty , and Mr. Veasey ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo assist applicants for community development block grant recovery assistance not having traditionally accepted forms of documentation of ownership of property to prove such ownership, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Heirs Empowerment and Inheritance Rights Act of 2025 or the HEIR Act of 2025 .\n#### 2. CDBG-Disaster Recovery and CDBG-Mitigation programs\n##### (a) Documentation of property ownership\n**(1) In general**\nThe Secretary of Housing and Urban Development shall amend the regulations at part 570 of title 24, Code of Federal Regulations, to ensure that in providing assistance for the Community Development Block Grant program for Disaster Recovery (CDBG\u2013DR) and the Community Development Block Grant program for Mitigation (CDBG\u2013MIT), in connection with a Presidentially declared disaster, in a case in which a homeowner is required to demonstrate ownership of a property heir property owners and any other owners not having traditionally accepted forms of documentation of ownership of property are provided resources and options for proving ownership for purposes of receiving assistance under such Disaster Recovery and Mitigation programs.\n**(2) Acceptable Documentation**\nAcceptable documentation for purposes paragraph (1) shall include\u2014\n**(A)**\na signed affidavit of ownership form developed pursuant to subsection (b); or\n**(B)**\nletters from local public or private schools, Federal or State benefit providers, and social service organizations, including community assistance programs and nonprofit organizations.\n**(3) Definition**\nFor purposes of this subsection, the term heir property means residential property for which title passed by operation of law through intestacy and is held by two or more heirs as tenants in common.\n##### (b) Affidavit of ownership\n**(1) Development and use**\nThe Secretary of Housing and Urban Development shall amend the regulations at part 570 of title 24, Code of Federal Regulations, to provide for the use of a standardized affidavit of ownership form, to be developed by the Secretary, by grantees of the Community Development Block Grant program for Disaster Recovery (CDBG\u2013DR) and the Community Development Block Grant program for Mitigation (CDBG\u2013MIT) in coordination with appropriate authorities of the applicable jurisdiction. Each grantee shall ensure that, at the time of application for housing repair and reconstruction assistance or mitigation assistance under such programs\u2014\n**(A)**\neach applicant is informed of the existence of the affidavit of ownership and provided a copy at the time of application; and\n**(B)**\ncopies of the form in English, Spanish, and any other locally predominant languages of the Presidentially-declared disaster area are accessible to the applicant.\n**(2) Prohibition**\nA grantee may not require that the signed affidavit of ownership form of an applicant be notarized.\n##### (c) Exemption\nAn affidavit of ownership form shall be exempt from any public comment periods or publication notices under part 570 of title 24, Code of Federal Regulations.",
      "versionDate": "2025-02-26",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-05-12T19:09:26Z"
          },
          {
            "name": "Department of Housing and Urban Development",
            "updateDate": "2025-05-12T19:09:45Z"
          },
          {
            "name": "Housing finance and home ownership",
            "updateDate": "2025-05-12T19:09:15Z"
          },
          {
            "name": "Residential rehabilitation and home repair",
            "updateDate": "2025-05-12T19:09:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "Housing and Community Development",
        "updateDate": "2025-03-18T14:28:01Z"
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
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1607ih.xml"
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
      "title": "HEIR Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:58:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HEIR Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Heirs Empowerment and Inheritance Rights Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To assist applicants for community development block grant recovery assistance not having traditionally accepted forms of documentation of ownership of property to prove such ownership, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:34Z"
    }
  ]
}
```
