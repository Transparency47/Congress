# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7359?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7359
- Title: Somalia Immigration Moratorium Act
- Congress: 119
- Bill type: HR
- Bill number: 7359
- Origin chamber: House
- Introduced date: 2026-02-04
- Update date: 2026-05-08T08:05:46Z
- Update date including text: 2026-05-08T08:05:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-04: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-02-04 - IntroReferral: Sponsor introductory remarks on measure. (CR H2015)
- Latest action: 2026-02-04: Introduced in House

## Actions

- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2026-02-04 - IntroReferral: Sponsor introductory remarks on measure. (CR H2015)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-04",
    "latestAction": {
      "actionDate": "2026-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7359",
    "number": "7359",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "G000603",
        "district": "26",
        "firstName": "Brandon",
        "fullName": "Rep. Gill, Brandon [R-TX-26]",
        "lastName": "Gill",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Somalia Immigration Moratorium Act",
    "type": "HR",
    "updateDate": "2026-05-08T08:05:46Z",
    "updateDateIncludingText": "2026-05-08T08:05:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-04",
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
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2026-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H2015)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-04",
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
          "date": "2026-02-04T15:00:40Z",
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
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "IL"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "FL"
    },
    {
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "AZ"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "LA"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "TX"
    },
    {
      "bioguideId": "F000485",
      "district": "14",
      "firstName": "Clay",
      "fullName": "Rep. Fuller, Clay [R-GA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Fuller",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "GA"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-05-07",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7359ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7359\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2026 Mr. Gill of Texas (for himself, Mrs. Miller of Illinois , Mr. Fine , Mr. Biggs of Arizona , and Mr. Higgins of Louisiana ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend section 212 of the Immigration and Nationality Act to prohibit immigration relief for certain citizens or nationals of Somalia.\n#### 1. Short title\nThis Act may be cited as the Somalia Immigration Moratorium Act .\n#### 2. Findings and purpose\n##### (a) Findings\nCongress finds the following:\n**(1)**\nIt is the purpose of the United States Government to guarantee survival and safety of the United States as an independent, sovereign republic whose government secures the God-given natural rights of its citizens and prioritizes their wellbeing and interests.\n**(2)**\nThe United States Government reserves the sovereign right to admit or deny entry into the United States any foreign person.\n##### (b) Purpose\nThe purpose of this Act is to establish a moratorium on immigration concerning citizens and nationals of Somalia.\n#### 3. Prohibition on immigration relief for certain citizens or nationals of Somalia\n##### (a) In general\nSection 212(a) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a) ) is amended by inserting at the end the following:\n(11) Nationals of somalia (A) In general Notwithstanding any other provision of law, except as provided in subparagraph (B), no alien may be issued a visa or provided any status under the immigration laws, until 25 years following the date of enactment of the Somalia Immigration Moratorium Act. (B) Exceptions Subparagraph (A) shall not apply to the following: (i) Any alien lawfully admitted to the United States prior to the date of enactment of Somalia Immigration Moratorium Act. (ii) Any lawful permanent resident of the United States. (iii) Any alien traveling with valid nonimmigrant visa in the following classifications: A\u20131, A\u20132, C\u20132, C\u20133, G\u20131, G\u20132, G\u20133, or G\u20134. These exceptions shall be made by only the Secretary of State or his or her designee, in coordination with the Secretary of Homeland Security or his or her designee. .\n##### (b) Ineligibility for relief\nSection 241(b)(3) of the Immigration and Nationality Act ( 8 U.S.C. 1231(b)(3) ) is amended by inserting at the end the following:\n(D) Ineligibility for relief Any alien who is a citizen or national of Somalia. .\n#### 4. Severability\nIf any provision of this Act, an amendment by this Act, or the application of such provision or amendment to any person or circumstance is held to be unconstitutional, the remainder of this Act, the amendments made by this Act, and the application of such provision or amendment to any person or circumstance shall not be affected thereby.",
      "versionDate": "2026-02-04",
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
        "updateDate": "2026-02-25T16:28:06Z"
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
      "date": "2026-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7359ih.xml"
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
      "title": "Somalia Immigration Moratorium Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T04:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Somalia Immigration Moratorium Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T04:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend section 212 of the Immigration and Nationality Act to prohibit immigration relief for certain citizens or nationals of Somalia.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T04:03:36Z"
    }
  ]
}
```
