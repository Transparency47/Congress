# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6032?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6032
- Title: Headstones for Honor Act
- Congress: 119
- Bill type: HR
- Bill number: 6032
- Origin chamber: House
- Introduced date: 2025-11-12
- Update date: 2026-01-21T09:05:30Z
- Update date including text: 2026-01-21T09:05:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-12: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-11-17 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-11-12: Introduced in House

## Actions

- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-11-17 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-12",
    "latestAction": {
      "actionDate": "2025-11-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6032",
    "number": "6032",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "H001066",
        "district": "4",
        "firstName": "Steven",
        "fullName": "Rep. Horsford, Steven [D-NV-4]",
        "lastName": "Horsford",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Headstones for Honor Act",
    "type": "HR",
    "updateDate": "2026-01-21T09:05:30Z",
    "updateDateIncludingText": "2026-01-21T09:05:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-17",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-12",
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
      "actionDate": "2025-11-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-12",
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
          "date": "2025-11-12T17:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-11-17T18:36:18Z",
              "name": "Referred to"
            }
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "NE"
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
      "sponsorshipDate": "2026-01-20",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6032ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6032\nIN THE HOUSE OF REPRESENTATIVES\nNovember 12, 2025 Mr. Horsford (for himself and Mr. Bacon ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to direct the Secretary of Veterans Affairs to furnish headstones, markers, and medallions for graves of certain enslaved individuals and individuals who performed military functions despite ineligibility to serve in the Armed Forces.\n#### 1. Short title\nThis Act may be cited as the Headstones for Honor Act .\n#### 2. Eligibility for headstones, markers, and medallions, furnished by the Secretary of Veterans Affairs, for graves of certain enslaved individuals and individuals who performed military functions despite ineligibility to serve in the Armed Forces\n##### (a) Establishment\nSection 2306 of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (3), by inserting and Navies after Armies ; and\n**(B)**\nby inserting, after paragraph (5), the following new paragraphs:\n(6) Any enslaved individual, determined by the Secretary to have\u2014 (A) accompanied a member of the Armed Forces or a Civil War veteran (as that term is defined in section 1501 of this title) during active military or naval service of such member or Civil War veteran; or (B) served in the Armed Forces (or Confederate Army or Navy) in lieu of another individual. (7) Any individual determined by the Secretary to have performed a military function while prohibited from serving as a member of the Armed Forces\u2014 (A) by Federal, State, or Tribal law; and (B) on the basis of race, gender, sex, or ethnicity. ;\n**(2)**\nin subsection (d)(1), by striking or (5) and inserting , (5), (6), or (7) ;\n**(3)**\nby redesignating subsections (j) and (k) as subsections (l) and (m), respectively; and\n**(4)**\nby inserting after subsection (i) the following new subsections:\n(j) With respect to an individual described in paragraph (6) of subsection (a), who served in the military or naval forces of the Confederate States of America during the Civil War, a headstone, marker, or medallion, furnished by the Secretary, shall include language that denotes such individual was forced to support their own enslavement. (k) With respect to an individual described in paragraph (6) or (7) of subsection (a), a request to the Secretary for a headstone, marker, or medallion may be made only by\u2014 (1) a direct descendant of the individual described in such paragraph; or (2) an individual whom the Secretary determines has made a sufficiently reasonable attempt to solicit, from such a known direct descendant, consent to make such request on behalf of such direct descendant. .\n##### (b) Regulations\nNot later than one year after the date of the enactment of this Act, the Secretary of Veterans Affairs shall prescribe regulations to implement the amendments made by subsection (a). Such regulations shall\u2014\n**(1)**\nbe informed by comment, solicited by the Secretary, from\u2014\n**(A)**\nCivil War historians;\n**(B)**\ncivil rights organizations; and\n**(C)**\ndirect descendants of individuals described in under paragraphs (6) and (7) of section 2306(a) of title 38, United States Code (as added by such subsection);\n**(2)**\ndefine the term military function for purposes of such section; and\n**(3)**\nestablish what evidence the Secretary may consider when determining the performance of military functions of such individuals or family relationships to such individuals, which shall include\u2014\n**(A)**\nFederal or State pay records;\n**(B)**\nFederal or State pension records;\n**(C)**\nConfederate pay records;\n**(D)**\nregimental histories;\n**(E)**\nnewspapers;\n**(F)**\nphotographs;\n**(G)**\nship logs;\n**(H)**\ndiaries;\n**(I)**\nfamily records, including bibles; and\n**(J)**\nchurch records.\n##### (c) Effective date\nThe amendments made by subsection (a) shall take effect on the earlier of\u2014\n**(1)**\nthe date on which the Secretary prescribes regulations under subsection (b); and\n**(2)**\nthe date that is one year after the date of the enactment of this Act.\n##### (d) Report\nNot later than 15 months after the date of the enactment of this Act, the Secretary shall submit to the Committees on Veterans\u2019 Affairs of the Senate and the House of Representatives a report on the implementation of the amendments made by subsection (a) and the regulations prescribed under subsection (b).",
      "versionDate": "2025-11-12",
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
        "updateDate": "2025-11-25T19:16:00Z"
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
      "date": "2025-11-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6032ih.xml"
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
      "title": "Headstones for Honor Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-13T12:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Headstones for Honor Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-13T12:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to direct the Secretary of Veterans Affairs to furnish headstones, markers, and medallions for graves of certain enslaved individuals and individuals who performed military functions despite ineligibility to serve in the Armed Forces.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-13T12:18:33Z"
    }
  ]
}
```
