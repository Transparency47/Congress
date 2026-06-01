# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6377?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6377
- Title: This act may be cited as the “Gold Star Siblings Educational Benefits Act
- Congress: 119
- Bill type: HR
- Bill number: 6377
- Origin chamber: House
- Introduced date: 2025-12-03
- Update date: 2026-01-09T09:07:05Z
- Update date including text: 2026-01-09T09:07:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-03: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-05 - Committee: Referred to the Subcommittee on Economic Opportunity.
- Latest action: 2025-12-03: Introduced in House

## Actions

- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-05 - Committee: Referred to the Subcommittee on Economic Opportunity.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6377",
    "number": "6377",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001285",
        "district": "26",
        "firstName": "Julia",
        "fullName": "Rep. Brownley, Julia [D-CA-26]",
        "lastName": "Brownley",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "This act may be cited as the \u201cGold Star Siblings Educational Benefits Act",
    "type": "HR",
    "updateDate": "2026-01-09T09:07:05Z",
    "updateDateIncludingText": "2026-01-09T09:07:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-05",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-03",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-03",
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
          "date": "2025-12-03T15:05:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-05T14:12:05Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "IN"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6377ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6377\nIN THE HOUSE OF REPRESENTATIVES\nDecember 3, 2025 Ms. Brownley introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to provide for the eligibility of siblings of certain veterans for educational assistance under the educational assistance programs of the Department of Veterans Affairs.\n#### 1. Short title\nThis Act may be cited as the This act may be cited as the \u201cGold Star Siblings Educational Benefits Act .\n#### 2. Eligibility of siblings of certain veterans for educational assistance under Department of Veterans Affairs Survivors\u2019 and Dependents\u2019 Educational Assistance Program\n##### (a) Eligibility\nParagraph (1) of subsection (a) of section 3501 of title 38, United States Code, is amended\u2014\n**(1)**\nin subparagraph (B), by inserting or sibling after spouse ;\n**(2)**\nin subparagraph (C), by striking spouse or child and inserting spouse, child, or sibling ;\n**(3)**\nin subparagraph (D), by inserting or sibling after spouse both places it appears; and\n**(4)**\nin subparagraph (E), by striking spouse or child and inserting spouse, child, or sibling .\n##### (b) Sibling defined\nSuch subsection is further amended by adding at the end the following new paragraph:\n(13) The term sibling means a brother or sister, whether by blood, adoption, or through a recognized guardianship or family relationship. .\n#### 3. Eligibility of siblings of certain veterans for educational assistance under Marine Gunnery Sergeant John David Fry scholarship\n##### (a) Eligibility\nEach of paragraphs (8), (9), and (10) of subsection (b) of section 3311 of title 38, United States Code, are amended by striking child or spouse and inserting child, spouse, or sibling .\n##### (b) Sibling defined\nParagraph (4) of subsection (f) of such section is amended to read as follows:\n(4) Definitions For purposes of paragraphs (8), (9), and (10) of subsection (b): (A) The term child includes a married individual or an individual who is above the age of twenty-three years. (B) The term sibling means a brother or sister, whether by blood, adoption, or through a recognized guardianship or family relationship. .\n#### 4. Eligibility of siblings of certain veterans for educational assistance transferred under Post-9/11 Educational Assistance Program\n##### (a) Eligibility\nSection 3319 of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (c)(2)\u2014\n**(A)**\nby striking has the meaning given the term dependent under subparagraphs (A), (I), and (D) of section 1072(2) of title 10. and inserting means an person who, with respect to an individual approved to transfer an entitlement to educational assistance under this section, is\u2014 ; and\n**(B)**\nby adding at the end the following new subparagraphs:\n(A) a dependent referred to in subparagraph (A), (D), or (I) of section 1072(2) of title 10; or (B) the sibling of the individual. ;\n**(2)**\nin subsection (g)\u2014\n**(A)**\nin paragraph (1), by inserting or a sibling 23 years of age or older after spouse ; and\n**(B)**\nin paragraph (2),\n**(i)**\nin the matter preceding subparagraph (A), by inserting or a sibling under the age of 23 after child ; and\n**(ii)**\nin subparagraph (B), by inserting or sibling after child both places it appears;\n**(3)**\nin subsection (h)\u2014\n**(A)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A)\u2014\n**(I)**\nby inserting or a sibling 23 years of age or older after a spouse ; and\n**(II)**\nby inserting or the sibling after the spouse ; and\n**(ii)**\nin subparagraph (B)\u2014\n**(I)**\nby inserting or a sibling under the age of 23 after a child ; and\n**(II)**\nby inserting or the sibling after the child ;\n**(B)**\nin paragraph (3)\u2014\n**(i)**\nin subparagraph (A), by inserting or a sibling 23 years of age or older after spouse ; and\n**(ii)**\nin subparagraph (B), by inserting or a sibling under the age of 23 after child ;\n**(C)**\nby redesignating paragraphs (6) and (7) as paragraphs (7) and (8), respectively; and\n**(D)**\nby inserting after paragraph (5) the following new paragraph (6):\n(6) Limitation on age of use by sibling transferees (A) In general Except as provided in subparagraphs (B) and (C), a sibling to whom entitlement is transferred under this section may use the benefits transferred until the later of the following dates: (i) The 15-year delimiting date specified in section 3321. (ii) The date on which the sibling attains the age of 26 years. (B) Primary caregivers of seriously injured members of the Armed Forces and veterans (i) In general Subject to clause (ii), in the case of a sibling who, before attaining the age of 26 years, is prevented from pursuing a chosen program of education by reason of acting as the primary provider of personal care services for a veteran or member of the Armed Forces under section 1720G(a) of this title, the sibling may use the benefits beginning on the date specified in clause (iii) for a period whose length is specified in clause (iv). (ii) Inapplicability for revocation Clause (i) shall not apply with respect to a period during which an individual acts as a primary provider of personal care services if the period concludes with the revocation of the individual\u2019s designation as such a primary provider under section 1720G(a)(7)(D) of this title. (iii) Date for commencement of use The date specified in this clause for the beginning of the use of benefits by a sibling under clause (i) is the later of\u2014 (I) the date on which the sibling ceases acting as the primary provider of personal care services for the veteran or member concerned as described in clause (i); (II) the date on which it is reasonably feasible, as determined under regulations prescribed by the Secretary, for the sibling to initiate or resume the use of benefits; or (III) the date on which the sibling attains the age of 26 years. (iv) Length of use The length of the period specified in this clause for the use of benefits by a sibling under clause (i) is the length equal to the length of the period that\u2014 (I) begins on the date on which the sibling begins acting as the primary provider of personal care services for the veteran or member concerned as described in clause (i); and (II) ends on the later of\u2014 (aa) the date on which the sibling ceases acting as the primary provider of personal care services for the veteran or member as described in clause (i); or (bb) the date on which it is reasonably feasible, as so determined, for the sibling to initiate or resume the use of benefits. .\n**(4)**\nby adding at the end the following new subsection:\n(m) Definition of sibling In this section, the term sibling means a brother or sister, whether by blood, adoption, or through a recognized guardianship or family relationship. .",
      "versionDate": "2025-12-03",
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
        "updateDate": "2025-12-19T17:35:45Z"
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
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6377ih.xml"
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
      "title": "This act may be cited as the \u201cGold Star Siblings Educational Benefits Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T05:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "This act may be cited as the \u201cGold Star Siblings Educational Benefits Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T05:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to provide for the eligibility of siblings of certain veterans for educational assistance under the educational assistance programs of the Department of Veterans Affairs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-19T05:03:52Z"
    }
  ]
}
```
