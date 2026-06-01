# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3080?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3080
- Title: Nitazene Sanctions Act
- Congress: 119
- Bill type: S
- Bill number: 3080
- Origin chamber: Senate
- Introduced date: 2025-10-30
- Update date: 2026-04-01T19:28:31Z
- Update date including text: 2026-04-01T19:28:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-30: Introduced in Senate
- 2025-10-30 - IntroReferral: Introduced in Senate
- 2025-10-30 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-10-30: Introduced in Senate

## Actions

- 2025-10-30 - IntroReferral: Introduced in Senate
- 2025-10-30 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-30",
    "latestAction": {
      "actionDate": "2025-10-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3080",
    "number": "3080",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Nitazene Sanctions Act",
    "type": "S",
    "updateDate": "2026-04-01T19:28:31Z",
    "updateDateIncludingText": "2026-04-01T19:28:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-30",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-30",
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
          "date": "2025-10-30T16:59:34Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-10-30",
      "state": "MO"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-10-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3080is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3080\nIN THE SENATE OF THE UNITED STATES\nOctober 30, 2025 Mr. Ricketts (for himself, Mr. Schmitt , and Mr. McCormick ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Fentanyl Sanctions Act to address nitazene trafficking and to impose sanctions with respect to entities of the People's Republic of China and foreign governments engaged in or contributing to opioid trafficking, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Nitazene Sanctions Act .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\n2-Benzylbenzimidazole opioids (also known as nitazenes) are a class of synthetic opioids first synthesized in the 1950s that exhibit significant potency at the mu-opioid receptor, with some substances exceeding the potency of fentanyl.\n**(2)**\nUnlike opium, 2-benzylbenzimidazole opioids and other synthetic opioids can be produced anywhere in the world using precursor chemicals that are often uncontrolled and widely available.\n**(3)**\nChemical manufacturing companies in the People\u2019s Republic of China can synthesize 2-benzylbenzimidazole opioid precursors at a scale using a comparatively easy 3- or 4-step process.\n**(4)**\nThe Drug Enforcement Administration has warned that Mexican cartels could use their existing relations with suppliers based in the People\u2019s Republic of China to obtain 2-benzylbenzimidazole opioids and funnel them into the United States.\n#### 3. Strategy to combat production and flow of nitazene\n##### (a) In general\nNot later than 120 days after the date of the enactment of this Act, the Secretary of State and the Attorney General shall jointly submit to the appropriate committees of Congress a report that includes\u2014\n**(1)**\na description of the role of the People's Republic of China, and of financial institutions in the People's Republic of China, in the production of 2-benzylbenzimidazole opioid precursors;\n**(2)**\na plan for steps to be taken by the United States Government to work with the People's Republic of China to reduce the production of such precursors in the People's Republic of China; and\n**(3)**\na strategy to work with allies in Europe to combat the flow of 2-benzylbenzimidazole opioids from the People's Republic of China.\n##### (b) Form\nThe report required by subsection (a) shall be submitted in unclassified form, but may include a classified annex.\n##### (c) Appropriate committees of Congress defined\nIn this section, the term appropriate committees of Congress means\u2014\n**(1)**\nthe Committee on Foreign Relations and the Committee on the Judiciary of the Senate; and\n**(2)**\nthe Committee on Foreign Affairs and the Committee on the Judiciary of the House of Representatives.\n#### 4. Inclusion of nitazene in Fentanyl Sanctions Act\nSection 7203(8)(A) of the Fentanyl Sanctions Act ( 21 U.S.C. 2302(8)(A) ) is amended\u2014\n**(1)**\nin clause (i), by striking controlled substances that are synthetic opioids and inserting 2-benzylbenzimidazole opioids, other controlled substances that are synthetic opioids, ; and\n**(2)**\nin clause (ii), by striking controlled substances and inserting 2-benzylbenzimidazole opioids and other controlled substances .\n#### 5. Designation of certain entities of the People's Republic of China as foreign opioid traffickers under Fentanyl Sanctions Act\n##### (a) In general\nSection 7203(5) of the Fentanyl Sanctions Act ( 21 U.S.C. 2302(5) ) is amended\u2014\n**(1)**\nby striking The term foreign opioid trafficker means any foreign person and inserting the following:\nThe term foreign opioid trafficker \u2014 (A) means any foreign person ;\n**(2)**\nby striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(B) includes\u2014 (i) any entity of the People\u2019s Republic of China that the President determines\u2014 (I) produces, manufactures, distributes, sells, or knowingly finances or transports any goods described in clause (i) or (ii) of paragraph (8)(A); and (II) fails to take credible steps, including through implementation of appropriate know-your-customer procedures or through cooperation with United States counternarcotics efforts, to detect or prevent opioid trafficking; and (ii) any senior official of the Government of the People\u2019s Republic of China or other political official of the People's Republic of China that\u2014 (I) has significant regulatory or law enforcement responsibilities with respect to the activities of an entity described in clause (i); and (II) aids and abets, including through intentional inaction, opioid trafficking. .\n##### (b) Assessment of certain agencies of the People's Republic of China as foreign opioid traffickers\nSection 7211(a)(1)(A) of the Fentanyl Sanctions Act ( 21 U.S.C. 2311(a)(1)(A) ) is amended by adding at the end before the semicolon the following: , including whether the heads of the National Narcotics Control Commission, the Ministry of Public Security, the General Administration of Customs, and the National Medical Products Administration of the Government of the People\u2019s Republic of China are foreign opioid traffickers .\n#### 6. Imposition of sanctions with respect to foreign governments contributing to opioid trafficking\nSection 7212 of the Fentanyl Sanctions Act ( 21 U.S.C. 2312 ) is amended\u2014\n**(1)**\nby striking The President and inserting the following:\n(a) Foreign opioid traffickers The President ; and\n**(2)**\nby adding at the end the following:\n(b) Foreign governments The President may impose one or more of the sanctions described in section 7213 with respect to each political subdivision, agency, or instrumentality of a foreign government, including any financial institution owned or controlled by a foreign government, that the President determines has knowingly on or after the date of the enactment of the Nitazene Sanctions Act \u2014 (1) engaged in a significant activity or a significant financial transaction that has materially contributed to opioid trafficking; (2) provided support for industries involved in the development of precursors for synthetic opioids; or (3) provided support for the transport of such precursors. .\n#### 7. Extension of Fentanyl Sanctions Act\nSection 7211(c) of the Fentanyl Sanctions Act ( 21 U.S.C. 2311(c) ) is amended by striking 5 years and inserting 10 years .",
      "versionDate": "2025-10-30",
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
        "name": "International Affairs",
        "updateDate": "2026-04-01T19:28:31Z"
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
      "date": "2025-10-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3080is.xml"
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
      "title": "Nitazene Sanctions Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-05T03:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Nitazene Sanctions Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-05T03:53:12Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Fentanyl Sanctions Act to address nitazene trafficking and to impose sanctions with respect to entities of the People's Republic of China and foreign governments engaged in or contributing to opioid trafficking, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-05T03:48:20Z"
    }
  ]
}
```
