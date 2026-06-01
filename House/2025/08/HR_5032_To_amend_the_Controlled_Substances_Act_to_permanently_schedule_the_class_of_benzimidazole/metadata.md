# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5032?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5032
- Title: Nitazene Control Act
- Congress: 119
- Bill type: HR
- Bill number: 5032
- Origin chamber: House
- Introduced date: 2025-08-22
- Update date: 2026-02-21T09:05:31Z
- Update date including text: 2026-02-21T09:05:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-22: Introduced in House
- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-22 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-08-22: Introduced in House

## Actions

- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Introduced in House
- 2025-08-22 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-22 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-22",
    "latestAction": {
      "actionDate": "2025-08-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5032",
    "number": "5032",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "V000138",
        "district": "7",
        "firstName": "Eugene",
        "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
        "lastName": "Vindman",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Nitazene Control Act",
    "type": "HR",
    "updateDate": "2026-02-21T09:05:31Z",
    "updateDateIncludingText": "2026-02-21T09:05:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-22",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-22",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-22",
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
          "date": "2025-08-22T13:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-08-22T13:01:15Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "WA"
    },
    {
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert F. [R-MO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "MO"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5032ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5032\nIN THE HOUSE OF REPRESENTATIVES\nAugust 22, 2025 Mr. Vindman (for himself and Mr. Baumgartner ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Controlled Substances Act to permanently schedule the class of benzimidazole-opioids known as nitazenes, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Nitazene Control Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nNitazenes are a class of synthetic opioids first synthesized in the 1950s that exhibit extreme potency at the mu-opioid receptor, with some analogs exceeding the potency of fentanyl.\n**(2)**\nThe Drug Enforcement Administration (DEA) has temporarily or permanently scheduled multiple nitazene compounds under Schedule I of the Controlled Substances Act due to their high abuse potential and lack of accepted medical use.\n**(3)**\nNitazenes and nitazene analogues have emerged in the illicit drug supply as designer drugs and contribute to overdose and fatal poisonings in the United States.\n**(4)**\nA class-wide permanent scheduling of nitazenes is necessary to preemptively address the proliferation of new analogs, streamline enforcement, and protect public health.\n#### 3. Schedule I classification of nitazenes\n##### (a) Amendment\nSection 202(c) of the Controlled Substances Act ( 21 U.S.C. 812(c) ) is amended by adding at the end of Schedule I the following:\n(f) Benzimidazole-opioids, commonly referred to as nitazenes, including any substance (including its salts, isomers, and salts of isomers) that has a chemical structure that is substantially similar to that of etonitazene or isotonitazene, including: (1) A benzimidazole core substituted at the 2-position with a benzyl or substituted benzyl group; and (2) A basic nitrogen-containing side chain at the 1-position; and (3) Exhibits agonist activity at the mu-opioid receptor. Such substances include, but are not limited to: etonitazene, clonitazene, metonitazene, isotonitazene, protonitazene, butonitazene, etodesnitazene, flunitazene, N-pyrrolidino etonitazene, N-desethyl isotonitazene, and N-piperidinyl etonitazene. .\n##### (b) Removal of temporary status\nAny substance included in the amendment to section 202(c) of the Controlled Substances Act made by this section that was temporarily scheduled under section 201(h) of the Controlled Substances Act shall be deemed permanently scheduled and subject to the requirements of Schedule I as of the date of enactment of this Act.\n##### (c) Rulemaking authority\nThe Attorney General, in consultation with the Secretary of Health and Human Services, may issue rules to clarify the scope of the nitazene class as necessary to enforce this section, provided such rules are consistent with the chemical definition in subsection (a)(1).\n##### (d) Research exemption\n**(1)**\nNotwithstanding the amendments made by subsection (a), a researcher who, as of the date of enactment of this Act, is conducting research involving a substance described in subsection (a) that was not previously listed in Schedule I of section 202(c) of the Controlled Substances Act ( 21 U.S.C. 812(c) ), shall not be required to obtain a registration under section 303(f) of such Act ( 21 U.S.C. 823(f) ) solely due to the inclusion of that substance in Schedule I, provided that:\n**(A)**\nthe research is being conducted pursuant to an active investigational new drug (IND) application or other applicable regulatory exemption recognized by the Food and Drug Administration or Drug Enforcement Administration;\n**(B)**\nthe research was approved by an institutional review board (IRB) prior to the enactment of this Act; and\n**(C)**\nthe researcher notifies the Attorney General, in a manner determined by the Attorney General, within 90 days of enactment of this Act.\n**(2)**\nThe exemption under paragraph (1) shall remain in effect for a period not to exceed 18 months from the date of enactment, during which time the researcher may apply for a registration under section 303(f), and the Attorney General shall expedite such applications to ensure continuity of research.\n**(3)**\nNothing in this subsection shall be construed to authorize the initiation of new research using substances described in subsection (a) without proper registration and scheduling compliance.",
      "versionDate": "2025-08-22",
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
        "updateDate": "2025-09-19T16:51:26Z"
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
      "date": "2025-08-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5032ih.xml"
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
      "title": "Nitazene Control Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-23T08:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Nitazene Control Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-23T08:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Controlled Substances Act to permanently schedule the class of benzimidazole-opioids known as nitazenes, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-23T08:18:23Z"
    }
  ]
}
```
