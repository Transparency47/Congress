# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4081?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4081
- Title: Foreign Adversary Federal Offense Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4081
- Origin chamber: House
- Introduced date: 2025-06-23
- Update date: 2026-05-20T08:08:33Z
- Update date including text: 2026-05-20T08:08:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-23: Introduced in House
- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-06-23: Introduced in House

## Actions

- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-23",
    "latestAction": {
      "actionDate": "2025-06-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4081",
    "number": "4081",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "H001101",
        "district": "10",
        "firstName": "Pat",
        "fullName": "Rep. Harrigan, Pat [R-NC-10]",
        "lastName": "Harrigan",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Foreign Adversary Federal Offense Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:33Z",
    "updateDateIncludingText": "2026-05-20T08:08:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-23",
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
      "actionDate": "2025-06-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-23",
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
          "date": "2025-06-23T16:03:20Z",
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
      "bioguideId": "K000405",
      "district": "13",
      "firstName": "Brad",
      "fullName": "Rep. Knott, Brad [R-NC-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Knott",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "NC"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "IN"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "NC"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "OH"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "KS"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "TX"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "NC"
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
      "sponsorshipDate": "2026-05-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4081ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4081\nIN THE HOUSE OF REPRESENTATIVES\nJune 23, 2025 Mr. Harrigan (for himself, Mr. Knott , and Mr. Baird ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to establish mandatory minimum penalties for economic and defense espionage when committed on behalf of foreign adversaries.\n#### 1. Short title\nThis Act may be cited as the Foreign Adversary Federal Offense Act of 2025 .\n#### 2. Economic espionage\nSection 1831 of title 18, United States Code, is amended\u2014\n**(1)**\nin subsection (a), in the matter following paragraph (5), by striking except as provided in subsection (b), and inserting except as provided in subsection (b) or (c), ; and\n**(2)**\nby adding at the end the following:\n(c) Special penalties The following additional penalties shall apply in the case of an offense under subsection (a): (1) Whoever commits such an offense to advance the interests of a covered nation (as such term is defined in section 4872 of title 10) shall, except as otherwise provided in paragraph (2), be\u2014 (A) fined not more than $5,000,000 or imprisoned not less than 10 years and not more than 15 years, or both, and shall be ineligible for supervised release; or (B) if the offense resulted in severe harm to economic or national security fined not more than $5,000,000 or imprisoned not less than 10 years and not more than 20 years, or both, and shall be ineligible for supervised release. (2) In the case of an organization that commits such an offense to advance the interests of a covered nation (as such term is defined in section 4872 of title 10), such organization shall be fined not more than the greater of $20,000,000 or 5 times the value of the stolen trade secret to the organization, including expenses for research and design and other costs of reproducing the trade secret that the organization has thereby avoided. (d) Severe harm to economic or national security For purposes of subsection (c), an offense will be considered to have resulted in severe harm to economic or national security if the offense was relating to the transmission of any nonpublic information relating to the security, design, operation, or vulnerability of critical infrastructure as defined in section 1016(e) of the Uniting and Strengthening America by Providing Appropriate Tools Required to Intercept and Obstruct Terrorism (USA PATRIOT ACT) Act of 2001 ( 42 U.S.C. 5195c(e) ) and where such information, if acted upon, would pose a significant threat of the incapacitation or destruction of such infrastructure. .\n#### 3. Gathering, transmitting or losing defense information\nSection 793 of title 18, United States Code, is amended, in the matter following subsection (f), by inserting after imprisoned not more than ten years, or both the following: , except that, if the violation of any of the foregoing provisions of this section was committed to advance the interests of a covered nation (as such term is defined in section 4872 of title 10), then the offender shall be fined under this title or imprisoned not less than 15 years and not more than any term of years or for life, or both .",
      "versionDate": "2025-06-23",
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
        "updateDate": "2025-07-16T13:08:57Z"
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
      "date": "2025-06-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4081ih.xml"
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
      "title": "Foreign Adversary Federal Offense Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-08T04:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Foreign Adversary Federal Offense Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to establish mandatory minimum penalties for economic and defense espionage when committed on behalf of foreign adversaries.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T04:33:28Z"
    }
  ]
}
```
