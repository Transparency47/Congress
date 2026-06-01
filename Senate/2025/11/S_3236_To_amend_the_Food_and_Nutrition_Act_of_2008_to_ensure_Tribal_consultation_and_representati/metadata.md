# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3236?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3236
- Title: Increasing Tribal Input on Nutrition Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3236
- Origin chamber: Senate
- Introduced date: 2025-11-20
- Update date: 2025-12-05T16:10:40Z
- Update date including text: 2025-12-05T16:10:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in Senate
- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-11-20: Introduced in Senate

## Actions

- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3236",
    "number": "3236",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "F000463",
        "district": "",
        "firstName": "Deb",
        "fullName": "Sen. Fischer, Deb [R-NE]",
        "lastName": "Fischer",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Increasing Tribal Input on Nutrition Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T16:10:40Z",
    "updateDateIncludingText": "2025-12-05T16:10:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-11-20T17:06:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MN"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CA"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "ND"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NV"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3236is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3236\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Mrs. Fischer (for herself, Ms. Smith , Mr. Schiff , Mr. Hoeven , Ms. Cortez Masto , and Mr. Bennet ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Food and Nutrition Act of 2008 to ensure Tribal consultation and representation under the food distribution program on Indian reservations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Increasing Tribal Input on Nutrition Act of 2025 .\n#### 2. Tribal consultation and representation; supply chain disruptions\n##### (a) Food distribution program on Indian reservations\nSection 4(b) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2013(b) ) is amended\u2014\n**(1)**\nby striking tribal organization each place it appears and inserting Tribal organization ;\n**(2)**\nby redesignating paragraph (7) as paragraph (9); and\n**(3)**\nby inserting after paragraph (6) the following:\n(7) Tribal inclusion in contracting process Prior to conducting evaluation of contracts under the food distribution program on Indian reservations under this subsection, the Secretary shall\u2014 (A) consult with Indian Tribes and Tribal organizations and ensure their feedback is integrated into the evaluation; and (B) consider feedback from Indian Tribes and Tribal organizations throughout the evaluation process. (8) Supply chain disruptions (A) Definition of supply chain disruption (i) In general In this paragraph, the term supply chain disruption means a shortage of foods that impedes the distribution of commodities, as determined by the Secretary. (ii) Inclusion The term supply chain disruption includes a supplemental food shortage due to a multifood warehouse issue that affects contracting, production, manufacture, sourcing, procurement, transportation, or storage of food and impedes the function of the food distribution program on Indian reservations under this subsection, as determined by the Secretary. (B) Emergency assistance If the Secretary determines that there is a supply chain disruption, the Secretary\u2014 (i) shall, not later than 45 days after the date on which the Secretary makes that determination, designate an emergency warehouse contractor to provide the required food capacity in a timely manner; and (ii) may provide direct payments or reimbursements to an Indian Tribe or Tribal organization administering the food distribution program on Indian reservations under this subsection to purchase food in accordance with subparagraph (D). (C) Payments The total amount of payments provided under subparagraph (B)(ii) to an Indian Tribe or Tribal organization shall not exceed the amount of funding that the Secretary would otherwise expend for that Indian Tribe or Tribal organization during the same time period under the food distribution program on Indian reservations under this subsection. (D) Procurement of agricultural commodities (i) In general Any agricultural commodities purchased by an Indian Tribe or Tribal organization using payments under subparagraph (B)(ii) shall satisfy the conditions described in clause (ii), unless waived by the Secretary. (ii) Conditions described The conditions referred to in clause (i) for agricultural commodities are the following: (I) The agricultural commodities are domestically produced. (II) The agricultural commodities supplant, not supplement, the type of agricultural commodities in existing food packages for that Indian Tribe or Tribal organization. (III) The agricultural commodities are of similar or higher nutritional value as the type of agricultural commodities that would be supplanted in the existing food package for that Indian Tribe or Tribal organization. (IV) The agricultural commodities meet any other criteria determined by the Secretary. (E) Notification; publication If the Secretary designates an emergency warehouse contractor under subparagraph (B)(i), the Secretary shall\u2014 (i) notify each affected Tribal organization or State agency of the designation, including an explanation of the determination of the Secretary of a supply chain disruption; and (ii) make that designation, and explanation of the determination, publicly available on the website of the Department of Agriculture. .\n##### (b) Commodity supplemental food program\nSection 5 of the Agriculture and Consumer Protection Act of 1973 ( 7 U.S.C. 612c note; Public Law 93\u201386 ) is amended by adding at the end the following:\n(n) Consultation with Indian Tribes (1) In general The Secretary shall implement the commodity supplemental food program in a manner that is responsive to the needs of the members of Indian Tribes and Tribal organizations by conducting annual consultations with Indian Tribes and Tribal organizations. (2) Amendments to State plans (A) In general With respect to submitting any amendment to a State plan pursuant to section 247.6 of title 7, Code of Federal Regulations (or a successor regulation), a State agency is encouraged\u2014 (i) prior to that submission, to consult in good faith with applicable Indian Tribes or Tribal organizations on the content of the amendment; and (ii) to include in the submission documentation evidencing that consultation. (B) Technical assistance The Secretary shall provide technical assistance to State agencies, including by entering into cooperative agreements, on how to properly conduct consultations pursuant to subparagraph (A), including relating to\u2014 (i) providing proper notice as to when a consultation will take place; (ii) ensuring consultations are with Tribal officials; and (iii) releasing a collaborative agenda in advance of the consultation. (o) Supply chain disruptions (1) Definition of supply chain disruption (A) In general In this paragraph, the term supply chain disruption means a shortage of foods that impedes the distribution of commodities, as determined by the Secretary. (B) Inclusion The term supply chain disruption includes a supplemental food shortage due to a multifood warehouse issue that affects contracting, production, manufacture, sourcing, procurement, transportation, or storage of food and impedes the function of the commodity supplemental food program, as determined by the Secretary. (2) Emergency warehouse contractor If the Secretary determines that there is a supply chain disruption, the Secretary shall, not later than 45 days after the date on which the Secretary makes that determination, designate an emergency warehouse contractor to provide the required food capacity in a timely manner. (3) Notification; publication If the Secretary designates an emergency warehouse contractor under paragraph (2), the Secretary shall\u2014 (A) notify each affected Tribal organization or State agency of the designation, including an explanation of the determination of the Secretary of a supply chain disruption; and (B) make that designation, and explanation of the determination, publicly available on the website of the Department of Agriculture. .",
      "versionDate": "2025-11-20",
      "versionType": "Introduced in Senate"
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
        "name": "Native Americans",
        "updateDate": "2025-12-05T16:10:40Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3236is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Increasing Tribal Input on Nutrition Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-05T04:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Increasing Tribal Input on Nutrition Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-05T04:08:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Food and Nutrition Act of 2008 to ensure Tribal consultation and representation under the food distribution program on Indian reservations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-05T04:03:50Z"
    }
  ]
}
```
