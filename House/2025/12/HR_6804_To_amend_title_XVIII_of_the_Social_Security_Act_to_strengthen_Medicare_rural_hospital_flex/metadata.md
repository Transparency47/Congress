# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6804?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6804
- Title: Rural Hospital Flexibility Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6804
- Origin chamber: House
- Introduced date: 2025-12-17
- Update date: 2026-04-17T08:07:15Z
- Update date including text: 2026-04-17T08:07:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-12-17: Introduced in House

## Actions

- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6804",
    "number": "6804",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001205",
        "district": "1",
        "firstName": "Carol",
        "fullName": "Rep. Miller, Carol D. [R-WV-1]",
        "lastName": "Miller",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "Rural Hospital Flexibility Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-17T08:07:15Z",
    "updateDateIncludingText": "2026-04-17T08:07:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-17",
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
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T14:05:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "AL"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "GA"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6804ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6804\nIN THE HOUSE OF REPRESENTATIVES\nDecember 17, 2025 Mrs. Miller of West Virginia (for herself and Ms. Sewell ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend title XVIII of the Social Security Act to strengthen Medicare rural hospital flexibility program grants.\n#### 1. Short title\nThis Act may be cited as the Rural Hospital Flexibility Act of 2025 .\n#### 2. Medicare rural hospital flexibility program grants\nSection 1820(g) of the Social Security Act ( 42 U.S.C. 1395i\u20134(g) ) is amended\u2014\n**(1)**\nby amending paragraph (1)(D) to read as follows:\n(D) providing support for critical access hospitals, certified rural health clinics, and rural emergency hospitals (as defined in section 1861(kkk)(2)) for quality improvement, quality reporting, performance improvements, benchmarking, addressing population health, transforming services, and providing linkages and services for behavioral health and substance use disorders responding to public health emergencies. ;\n**(2)**\nby redesignating paragraphs (3) through (7) as paragraphs (4) through (8), respectively;\n**(3)**\nafter paragraph (2), by inserting the following new paragraph:\n(3) Activities to support carrying out other grants The Secretary may award grants or cooperative agreements to entities awarded grants or agreements under other provisions of this subsection for purposes of supporting such entities in carrying out activities under such other grants or agreements by providing technical assistance, data analysis, and evaluation efforts. An entity seeking a grant under this paragraph shall submit an application to the Secretary at such time and in such manner as specified by the Secretary. ;\n**(4)**\nin paragraph (4), as redesignated\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nin the header, by striking hospitals and inserting State Offices of Rural Health ; and\n**(ii)**\nby striking grants to hospitals and inserting grants to State Offices of Rural Health ;\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nby redesignating clauses (i) and (ii) as subclauses (I) and (II), respectively;\n**(ii)**\nby striking means a non-Federal and inserting the following:\nmeans\u2014 (i) a non-Federal ; and\n**(iii)**\nby striking the period at the end and inserting the following:\n; or (ii) a rural emergency hospital (as defined in section 1861(kkk)). ;\n**(C)**\nby amending subparagraph (C) to read as follows:\n(C) Application The State Office of Rural Health shall submit an application to the Secretary on or before such date and in such form and manner as the Secretary specifies. ;\n**(D)**\nby amending subparagraph (D) to read as follows:\n(D) Amount of grant With respect to funds made available to make grants under this paragraph in a fiscal year, the amount awarded to a State Office of Rural Health shall bear the same ratio to the total amount of such funds so made available as the number of eligible small rural hospitals in such State bears to the total number of eligible small rural hospitals in all States receiving a grant under this paragraph for such fiscal year propose. ;\n**(E)**\nby amending subparagraph (E) to read as follows:\n(E) Use of funds State Offices of Rural Health may use the funds received through a grant under this paragraph for the purchase of computer software and hardware on behalf of eligible small rural hospitals, for the education and training of eligible small rural hospital staff on billing, operational, quality improvement, and related value-focused efforts, and for other delivery system reform programs determined appropriate by the Secretary. ; and\n**(F)**\nin subparagraph (F)\u2014\n**(i)**\nin clause (i), by striking A hospital receiving a grant under this section and inserting An entity receiving a grant under this paragraph ; and\n**(ii)**\nin clause (ii), by striking section each place such term appears and inserting paragraph in each such place;\n**(5)**\nin paragraph (5), as redesignated, by striking paragraph (1) or (2) and inserting paragraph (1), (2), or (4) ; and\n**(6)**\nby adding at the end the following new paragraphs:\n(9) Rural Health Transformation Grants (A) Grants The Secretary may award 5-year grants to State Offices of Rural Health and to eligible rural health care providers (as defined in subparagraph (D)) on the transition to new models, including rural emergency hospitals, extended stay clinics, freestanding emergency departments, rural health clinics, and integration of behavioral, oral health services, telehealth and other transformational models relevant to rural providers as such providers evolve to better meet community needs and the changing health care environment. (B) Application An eligible rural health care provider, in consultation with the State Office of Rural Health in the State in which the rural health care provider seeking a grant under this paragraph is located, shall submit an application to the Secretary on or before such date and in such form and manner as the Secretary specifies. (C) Additional requirements The Secretary may not award a grant under this paragraph to an eligible rural health care provider unless\u2014 (i) local organizations or the State in which the hospital is located provides support (either direct or in kind); and there are letters of support from key State payers such as Medicaid and private insurance; and (ii) the applicant describes in detail how the transition of the health care provider or providers will better meet local needs and be sustainable. (D) Eligible rural health care provider defined For purposes of this paragraph, the term eligible rural health care provider includes a critical access hospital, a certified rural health clinic, a rural nursing home, skilled nursing facility, emergency care provider, or other entity identified by the Secretary. An eligible rural health care provider may include other entities applying on behalf of a group of rural health care providers such as a State Office of Rural Health, a State or local health care authority, a rural health network, or other entity identified by the Secretary. (10) Rural emergency hospital technical assistance (A) In general The Secretary may award grants or cooperative agreements to eligible entities (as determined by the Secretary) for the purpose of providing technical assistance, data analysis, and other support to hospitals that are seeking to be designated, or are currently designated, as rural emergency hospitals (as described in section 1861(kkk)(2)). (B) Application An entity seeking a grant under subparagraph (A) shall submit an application to the Secretary at such time and in such form and manner as specified by the Secretary. .",
      "versionDate": "2025-12-17",
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
        "updateDate": "2026-02-18T19:18:08Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6804ih.xml"
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
      "title": "Rural Hospital Flexibility Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-10T06:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rural Hospital Flexibility Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-10T06:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to strengthen Medicare rural hospital flexibility program grants.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-10T06:03:26Z"
    }
  ]
}
```
