# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4019?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4019
- Title: Gio’s Law
- Congress: 119
- Bill type: HR
- Bill number: 4019
- Origin chamber: House
- Introduced date: 2025-06-17
- Update date: 2026-05-30T08:05:56Z
- Update date including text: 2026-05-30T08:05:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-17: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-06-17: Introduced in House

## Actions

- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-17",
    "latestAction": {
      "actionDate": "2025-06-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4019",
    "number": "4019",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "G000602",
        "district": "4",
        "firstName": "Laura",
        "fullName": "Rep. Gillen, Laura [D-NY-4]",
        "lastName": "Gillen",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Gio\u2019s Law",
    "type": "HR",
    "updateDate": "2026-05-30T08:05:56Z",
    "updateDateIncludingText": "2026-05-30T08:05:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-17",
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
      "actionDate": "2025-06-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-17",
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
          "date": "2025-06-17T15:02:10Z",
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
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "NY"
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
      "sponsorshipDate": "2025-07-02",
      "state": "PA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "IA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "NY"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "WI"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "NC"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-05-22",
      "state": "VA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "DC"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4019ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4019\nIN THE HOUSE OF REPRESENTATIVES\nJune 17, 2025 Ms. Gillen (for herself and Mr. Garbarino ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Omnibus Crime Control and Safe Streets Act of 1968 to establish a grant program for provide access to, and training on the administration of, epinephrine products for law enforcement officers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as Gio\u2019s Law .\n#### 2. Law Enforcement Access to Emergency Epinephrine Grant Program\nTitle I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10101 et seq. ) is amended by adding at the end the following:\nPP Law Enforcement Access to Emergency Epinephrine Grant Program 3061. Grant authorization The Attorney General is authorized to make grants under this part to States and units of local government to\u2014 (1) purchase epinephrine products for use by State, local, and tribal law enforcement agencies; (2) train State, local, and tribal law enforcement officers, in accordance with the curricula developed or identified under section 3062. 3062. Standardized training Not later than 180 days after the date of enactment of this part, the Attorney General shall develop a training curricula, or identify effective existing training curricula, to train law enforcement officer to\u2014 (1) recognize the symptoms of an anaphylactic reaction; and (2) correctly administer epinephrine products to any individual reasonably believed to be having an anaphylactic reaction. 3063. Application The chief executive of a State or unit of local government seeking a grant under this part shall submit to the Attorney General an application at such time, in such manner, and containing such information as the Attorney General may reasonably require, including a certification of the State attorney general of the State, or the State in which the unit of local government is located, that a law enforcement officer who is authorized in that jurisdiction to administer epinephrine products to any individual reasonably believed to be having an anaphylactic reaction is protected from civil liability arising from administering such a product. 3064. Definition In this part, the term epinephrine product means\u2014 (1) an epinephrine auto-injector; and (2) a product that facilitates the administration of epinephrine other than by injection. 3065. Authorization of appropriations There is authorized to be appropriated $25,000,000 to carry out this part for each of fiscal years 2026 through 2030. .\n#### 3. Report on administration of epinephrine by law enforcement officers\nOn an annual basis, the Attorney General, acting through the Director of the Bureau of Justice Statistics, shall submit to Congress and make publicly available, data on the frequency of the administration of epinephrine products (as such term is defined in section 3064 of title I of the Omnibus Crime Control and Safe Streets Act of 1968) by Federal, State, local, and tribal law enforcement officers.\n#### 4. Interagency Public Awareness and Outreach Campaign\nNot later than 180 days after the date of enactment of this Act, the Attorney General, in collaboration with the Secretary of Health and Human Services, shall design and implement a public awareness campaign to educate members of the public about\u2014\n**(1)**\nthe symptoms of an anaphylactic reaction; and\n**(2)**\nthe role of law enforcement officers and first responders in administering epinephrine products.",
      "versionDate": "2025-06-17",
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
        "updateDate": "2025-07-08T13:42:07Z"
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
      "date": "2025-06-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4019ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Gio\u2019s Law",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-25T07:43:21Z"
    },
    {
      "title": "Gio\u2019s Law",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-25T07:43:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Omnibus Crime Control and Safe Streets Act of 1968 to establish a grant program for provide access to, and training on the administration of, epinephrine products for law enforcement officers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-25T07:33:21Z"
    }
  ]
}
```
