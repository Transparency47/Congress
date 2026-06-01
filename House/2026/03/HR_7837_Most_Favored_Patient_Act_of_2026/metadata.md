# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7837?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7837
- Title: Most Favored Patient Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7837
- Origin chamber: House
- Introduced date: 2026-03-05
- Update date: 2026-03-10T12:05:31Z
- Update date including text: 2026-03-10T12:05:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-05: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-05 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-03-05: Introduced in House

## Actions

- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Introduced in House
- 2026-03-05 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-05 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-05",
    "latestAction": {
      "actionDate": "2026-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7837",
    "number": "7837",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001204",
        "district": "9",
        "firstName": "Daniel",
        "fullName": "Rep. Meuser, Daniel [R-PA-9]",
        "lastName": "Meuser",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Most Favored Patient Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-10T12:05:31Z",
    "updateDateIncludingText": "2026-03-10T12:05:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-05",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-05",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-05",
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
          "date": "2026-03-05T15:01:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-03-05T15:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7837ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7837\nMarch 5, 2026 Mr. Meuser introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XI of the Social Security Act to require the Center for Medicare and Medicaid Innovation to test a model implementing most-favored-nation drug pricing.\n#### 1. Short title\nThis Act may be cited as the Most Favored Patient Act of 2026 .\n#### 2. Requiring the Center for Medicare and Medicaid Innovation to test a model implementing most favored nation drug pricing\nSection 1115A of the Social Security Act ( 42 U.S.C. 1315a ) is amended\u2014\n**(1)**\nin subsection (b)(2)(A), by inserting , and, beginning January 1, 2029, shall include the Most Favored Nations Pricing Model described in subsection (h) before the period at the end; and\n**(2)**\nby adding at the end the following new subsection:\n(h) Most Favored Nations Pricing Model (1) In general For purposes of subsection (b)(2)(A), the Most Favored Nations Pricing Model described in this subsection is a model under which, subject to paragraph (2) , each specified manufacturer\u2014 (A) provides access to the most-favored-nation price of each covered drug of such manufacturer\u2014 (i) to most-favored-nation price eligible individuals who with respect to such drug are described in clause (i) of paragraph (5)(D) and are dispensed such drug (and to pharmacies, mail order services, and other dispensers, with respect to such individuals who are dispensed such drugs); and (ii) to hospitals, physicians, and other providers of services and suppliers with respect to most-favored-nation price eligible individuals who with respect to such drug are described in clause (ii) of such paragraph furnished or administered such drug; and (B) reports to the Secretary, at such time and in such manner as the Secretary shall specify, such information as the Secretary determines necessary for purposes of calculating the most-favored-nation price with respect to each such covered drug. (2) Exception The Secretary may suspend the requirements under paragraph (1) with respect to a covered drug of a specified manufacturer until April 1, 2029, if the Secretary reasonably believes that such manufacturer is likely to enter into a covered agreement with the Secretary before such date. (3) Duration The model described in paragraph (1) shall be carried out for a period of 5 years. (4) Definitions In this subsection: (A) Applicable net price The term applicable net price means, with respect to a covered drug and a reference country in which such drug was sold during a year, the average price paid to the manufacturer for the drug across package sizes and package types of the drug in such reference country during such year across all purchasers, taking into account all manufacturer rebates, discounts, and price concessions, and adjusted to take into account differences in purchasing power in such country compared to the United States in a manner specified by the Secretary. (B) Appropriate congressional committees The term appropriate congressional committees means\u2014 (i) the Committee on Energy and Commerce and the Committee on Ways and Means of the House of Representatives; and (ii) the Committee on Finance and the Committee on Health, Education, Labor, and Pensions of the Senate. (C) Covered agreement The term covered agreement means an agreement between a manufacturer of a covered drug and the Secretary that\u2014 (i) provides that such manufacturer\u2014 (I) will provide access to the most-favored-nation price of 1 or more covered drugs of such manufacturer in the same manner as described in paragraph (1)(A) ; (II) will report to the Secretary the information described in paragraph (1)(B) with respect to each such drug; and (III) commits, to the satisfaction of the Secretary, to increasing manufacturing operations in the United States; and (ii) is\u2014 (I) entered into not later than December 31, 2028; and (II) reported by the Secretary to the appropriate congressional committees\u2014 (aa) not later than April 1, 2029; or (bb) in the case that such agreement was entered into before the date of the enactment of the Most Favored Patient Act of 2026 , not later than the date that is 30 days after such date of enactment. (D) Covered drug The term covered drug means, with respect to a year, a specified drug that was sold in 2 or more reference countries during such year. (E) Manufacturer The term manufacturer has the meaning given such term in section 1847A(c)(6)(A). (F) Most-favored-nation price The term most-favored-nation price means, with respect to a covered drug and a year, the second-lowest applicable net price for such drug. (G) Most-favored-nation price eligible individual The term most-favored-nation price eligible individual means, with respect to a covered drug\u2014 (i) in the case such drug is dispensed to the individual at a pharmacy, by a mail order service, or by another dispenser, an individual\u2014 (I) who is eligible for medical assistance under a State plan (or a waiver of such plan) under title XIX if coverage is provided under such plan (or waiver) for such covered drug; or (II) who is enrolled in a prescription drug plan under part D of title XVIII or an MA\u2013PD plan under part C of such title if coverage is provided under such plan for such covered drug; and (ii) in the case such drug is furnished or administered to the individual by a hospital, physician, or other provider of services or supplier, an individual who is enrolled under part B of title XVIII, including an individual who is enrolled in an MA plan under part C of such title, if payment may be made under part B for such selected drug. (H) Reference country The term reference country means any of the following countries: (i) Canada. (ii) Denmark. (iii) France. (iv) Germany. (v) Italy. (vi) Japan. (vii) Switzerland. (viii) The United Kingdom. (I) Specified drug The term specified drug means\u2014 (i) a covered outpatient drug (as defined in section 1927(k)); (ii) a drug or biological product for which payment may be made under part B of title XVIII; or (iii) a covered part D drug (as defined in section 1860D\u20132(e)). (J) Specified manufacturer The term specified manufacturer means a manufacturer of a covered drug that does not have a covered agreement with the Secretary. .",
      "versionDate": "2026-03-05",
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
        "name": "Health",
        "updateDate": "2026-03-10T12:05:31Z"
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
      "date": "2026-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7837ih.xml"
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
      "title": "To amend title XI of the Social Security Act to require the Center for Medicare and Medicaid Innovation to test a model implementing most-favored-nation drug pricing.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-09T18:03:25Z"
    },
    {
      "title": "Most Favored Patient Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-06T10:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Most Favored Patient Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-06T10:53:20Z"
    }
  ]
}
```
