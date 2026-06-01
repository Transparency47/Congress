# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5767?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5767
- Title: Secure Commercial Driver Licensing Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5767
- Origin chamber: House
- Introduced date: 2025-10-17
- Update date: 2026-04-22T08:07:01Z
- Update date including text: 2026-04-22T08:07:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-17: Introduced in House
- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-12-01 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-10-17: Introduced in House

## Actions

- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-12-01 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-17",
    "latestAction": {
      "actionDate": "2025-10-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5767",
    "number": "5767",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "B001282",
        "district": "6",
        "firstName": "Andy",
        "fullName": "Rep. Barr, Andy [R-KY-6]",
        "lastName": "Barr",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Secure Commercial Driver Licensing Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-22T08:07:01Z",
    "updateDateIncludingText": "2026-04-22T08:07:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-01",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-17",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-17",
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
          "date": "2025-10-17T18:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-01T19:49:26Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "AL"
    },
    {
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "False",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "TX"
    },
    {
      "bioguideId": "L000583",
      "district": "11",
      "firstName": "Barry",
      "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Loudermilk",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "GA"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "TX"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "TX"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5767ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5767\nIN THE HOUSE OF REPRESENTATIVES\nOctober 17, 2025 Mr. Barr introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo require all testing relating to the issuance or renewal of a commercial driver\u2019s license to be conducted only in English, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Secure Commercial Driver Licensing Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Commercial driver\u2019s license**\nThe term commercial driver\u2019s license has the meaning given the term in section 31301 of title 49, United States Code.\n**(2) Driver\u2019s license**\nThe term driver\u2019s license has the meaning given the term in section 31301 of title 49, United States Code.\n**(3) Non-domiciled CDL**\nThe term non-domiciled CDL means a commercial driver\u2019s license issued by a State or other jurisdiction to an individual who is not domiciled in that State or jurisdiction, in accordance with part 383 of title 49, Code of Federal Regulations (or successor regulations).\n**(4) Non-domiciled CLP**\nThe term non-domiciled CLP means a commercial learner\u2019s permit issued by a State or other jurisdiction to an individual who is not domiciled in that State or jurisdiction, in accordance with part 383 of title 49, Code of Federal Regulations (or successor regulations).\n**(5) Secretary**\nThe term Secretary means the Secretary of Transportation.\n#### 3. Requirement to administer driving tests in English\n##### (a) In general\nSection 31305(a) of title 49, United States Code, is amended\u2014\n**(1)**\nin the matter preceding paragraph (1), in the first sentence, by inserting (referred to in this section as the Secretary ) after Secretary of Transportation ;\n**(2)**\nby redesignating paragraphs (7) and (8) as paragraphs (8) and (9), respectively; and\n**(3)**\nby inserting after paragraph (6) the following:\n(7) shall require the tests to be administered only in English; .\n##### (b) Rulemaking\nNot later than 180 days after the date of enactment of this Act, the Secretary shall promulgate new, or revise existing, regulations, rules, and documents, as necessary, to ensure that all testing relating to the issuance or renewal of a commercial driver\u2019s license is conducted only in English, including\u2014\n**(1)**\nany tests administered as part of an entry-level driver training program;\n**(2)**\nany knowledge tests relating to the issuance or renewal of a commercial driver\u2019s license; and\n**(3)**\nany tests administered by a third-party training provider included on the training provider registry maintained by the Federal Motor Carrier Safety Administration.\n#### 4. Requirement to hold driver\u2019s license before obtaining CDL\n##### (a) In general\nSubject to subsection (b), beginning on the date of enactment of this Act, a commercial driver\u2019s license may not be issued to an individual who has not held a driver\u2019s license for a period of at least 1 year before the date on which the commercial driver\u2019s license is issued.\n##### (b) Exemption\nSubsection (a) does not apply to an individual who holds a commercial driver\u2019s license as of the date of enactment of this Act.\n#### 5. Revocation of authority\nThe Secretary may revoke the authority of any State or other jurisdiction to issue non-domiciled CDLs or non-domiciled CLPs if the Secretary determines that the State or other jurisdiction is not in compliance with all applicable Federal standards relating to that authority, including the provisions of this Act and any regulations promulgated or revised under this Act.",
      "versionDate": "2025-10-17",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-10-16",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "3013",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Secure Commercial Driver Licensing Act of 2025",
      "type": "S"
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-12-08T16:36:58Z"
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
      "date": "2025-10-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5767ih.xml"
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
      "title": "Secure Commercial Driver Licensing Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-22T03:53:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Secure Commercial Driver Licensing Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-22T03:53:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require all testing relating to the issuance or renewal of a commercial driver's license to be conducted only in English, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-22T03:48:15Z"
    }
  ]
}
```
