# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4091?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4091
- Title: Habitat Connectivity on Working Lands Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4091
- Origin chamber: Senate
- Introduced date: 2026-03-12
- Update date: 2026-03-27T21:31:31Z
- Update date including text: 2026-03-27T21:31:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-12: Introduced in Senate
- 2026-03-12 - IntroReferral: Introduced in Senate
- 2026-03-12 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2026-03-12: Introduced in Senate

## Actions

- 2026-03-12 - IntroReferral: Introduced in Senate
- 2026-03-12 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-12",
    "latestAction": {
      "actionDate": "2026-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4091",
    "number": "4091",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "H001046",
        "district": "",
        "firstName": "Martin",
        "fullName": "Sen. Heinrich, Martin [D-NM]",
        "lastName": "Heinrich",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Habitat Connectivity on Working Lands Act of 2026",
    "type": "S",
    "updateDate": "2026-03-27T21:31:31Z",
    "updateDateIncludingText": "2026-03-27T21:31:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-12",
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
      "actionDate": "2026-03-12",
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
          "date": "2026-03-12T18:38:34Z",
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
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4091is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4091\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2026 Mr. Heinrich (for himself and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Food Security Act of 1985 to improve wildlife habitat connectivity and wildlife migration corridors, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Habitat Connectivity on Working Lands Act of 2026 .\n#### 2. Conservation programs\n##### (a) Definition of native big game species\nSection 1201(a) of the Food Security Act of 1985 ( 16 U.S.C. 3801(a) ) is amended\u2014\n**(1)**\nby redesignating paragraphs (18) through (27) as paragraphs (19) through (28), respectively; and\n**(2)**\nby inserting after paragraph (17) the following:\n(18) Native big game species The term native big game species means a native species of a large mammal, including a wild deer, an elk, a pronghorn, a wild sheep, and a moose. .\n##### (b) Regional Conservation Partnership Program critical conservation areas\nSection 1271F(a)(2)(C) of the Food Security Act of 1985 ( 16 U.S.C. 3871f(a)(2)(C) ) is amended by inserting , including restoration and enhancement of wildlife habitat connectivity and wildlife migration corridors, with a focus on native big game species before ; and .\n##### (c) Enrollment in the environmental quality incentives program and the conservation stewardship program of grassland enrolled in the conservation reserve program\n**(1) Environmental quality incentives program**\nSection 1240B(d) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20132(d) ) is amended\u2014\n**(A)**\nin paragraph (6), by striking A producer and inserting Except as provided in paragraph (8), a producer ; and\n**(B)**\nby adding at the end the following:\n(8) Cost-share payments for grassland enrolled in the conservation reserve program (A) In general The Secretary may provide payments under the program for costs associated with planning, design, materials, equipment, installation, labor, management, maintenance, or training with respect to eligible land that is\u2014 (i) enrolled in the conservation reserve program under section 1231(d)(2)(A); and (ii) of ecological significance, as described in section 1231(d)(2)(B)(iii). (B) Limitations (i) Other Federal programs A producer shall not be eligible for payments under subparagraph (A) for practices if the producer receives payments or other benefits for the same practice on the same land under another Federal program (other than the conservation reserve program under subchapter B of chapter 1). (ii) Protection of emergency grazing and haying An activity to restore or enhance wildlife habitat connectivity or wildlife migration corridors carried out using a payment under subparagraph (A) shall not prevent or alter emergency haying or emergency grazing carried out in accordance with the requirements of the conservation reserve program under subchapter B of chapter 1. .\n**(2) Conservation stewardship program**\nSection 1240J(b) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u201322(b) ) is amended\u2014\n**(A)**\nin paragraph (1), in the matter preceding subparagraph (A), by inserting and except as provided in paragraph (3), after paragraph (2), ; and\n**(B)**\nby adding at the end the following:\n(3) Cost-share payments for grassland enrolled in the conservation reserve program (A) In general The Secretary may provide payments under the program for costs associated with planning, design, materials, equipment, installation, labor, management, maintenance, or training with respect to eligible land that is\u2014 (i) enrolled in the conservation reserve program under section 1231(d)(2)(A); and (ii) of ecological significance, as described in section 1231(d)(2)(B)(iii). (B) Limitations (i) Other Federal programs A producer shall not be eligible for payments under subparagraph (A) for conservation activities if the producer receives payments or other benefits for the same conservation activities on the same land under another Federal program (other than the conservation reserve program under subchapter B of chapter 1). (ii) Protection of emergency grazing and haying An activity to restore or enhance wildlife habitat connectivity or wildlife migration corridors carried out using a payment under subparagraph (A) shall not prevent or alter emergency haying or emergency grazing carried out in accordance with the requirements of the conservation reserve program under subchapter B of chapter 1. .\n**(3) Payment limitation for rental payments under the conservation reserve program**\nSection 1234(g)(1) of the Food Security Act of 1985 ( 16 U.S.C. 3834(g)(1) ) is amended by striking $50,000 and inserting $125,000 .\n##### (d) Increased payments under the environmental quality incentives program\nSection 1240B(d) of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20132(d) ) is amended\u2014\n**(1)**\nin paragraph (3)(F), by inserting and wildlife habitat connectivity before ; or ; and\n**(2)**\nin paragraph (7)(A)\u2014\n**(A)**\nin clause (iii), by striking or at the end;\n**(B)**\nin clause (iv), by striking the period at the end and inserting ; or ; and\n**(C)**\nby adding at the end the following:\n(v) addresses the conservation and restoration of wildlife habitat, including wildlife habitat connectivity and wildlife migration corridors. .\n##### (e) Conservation practice standards\nSection 1242 of the Food Security Act of 1985 ( 16 U.S.C. 3842 ) is amended by adding at the end the following:\n(j) Addressing barriers to habitat connectivity (1) In general The Secretary shall\u2014 (A) to the maximum extent practicable, fully incorporate nonstructural methods to manage livestock distribution, such as virtual fencing, into the conservation practice standards; and (B) provide for the appropriate range of conservation practices and resource mitigation measures available to landowners using nonstructural methods described in subparagraph (A). (2) Availability of adequate technical assistance The Secretary shall ensure that adequate technical assistance is available for the implementation of\u2014 (A) nonstructural methods described in paragraph (1)(A); and (B) other practices that support habitat connectivity through Federal conservation programs. .\n##### (f) Administrative requirements for conservation programs\nSection 1244 of the Food Security Act of 1985 ( 16 U.S.C. 3844 ) is amended by adding at the end the following:\n(q) Encouragement of habitat connectivity and native big game migration corridors In carrying out any conservation program administered by the Secretary, the Secretary may, as appropriate, encourage\u2014 (1) the conservation of landscape corridors and hydrologic connectivity, where native big game species and ecological processes can transition from one habitat to another, in order to conserve native biodiversity and ensure resiliency against impacts from a range of stressors; and (2) the use of conservation practices that support the development, restoration, and maintenance of landscape corridors and hydrologic connectivity. .\n#### 3. High-priority research and extension areas\nSection 1672(d) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 5925(d) ) is amended by adding at the end the following:\n(21) Virtual fencing Research and extension grants may be made under this section for the purposes of\u2014 (A) understanding and addressing the barriers to the adoption of virtual fencing technology; or (B) studying the effects of virtual fencing technology on\u2014 (i) natural and cultural resources, such as\u2014 (I) sensitive riparian areas; and (II) crucial winter range and stopover habitats for native big game species (as defined in section 1201(a) of the Food Security Act of 1985 ( 16 U.S.C. 3801(a) )); or (ii) overall range health. .",
      "versionDate": "2026-03-12",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-03-27T21:31:30Z"
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
      "date": "2026-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4091is.xml"
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
      "title": "Habitat Connectivity on Working Lands Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-25T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Habitat Connectivity on Working Lands Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Food Security Act of 1985 to improve wildlife habitat connectivity and wildlife migration corridors, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-25T03:48:25Z"
    }
  ]
}
```
