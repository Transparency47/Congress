# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/860?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/860
- Title: BUST FENTANYL Act
- Congress: 119
- Bill type: S
- Bill number: 860
- Origin chamber: Senate
- Introduced date: 2025-03-05
- Update date: 2026-02-24T14:10:39Z
- Update date including text: 2026-02-24T14:10:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-05: Introduced in Senate
- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-03-27 - Committee: Committee on Foreign Relations. Ordered to be reported without amendment favorably.
- 2025-04-28 - Committee: Committee on Foreign Relations. Reported by Senator Risch without amendment. Without written report.
- 2025-04-28 - Committee: Committee on Foreign Relations. Reported by Senator Risch without amendment. Without written report.
- 2025-04-28 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 54.
- Latest action: 2025-03-05: Introduced in Senate

## Actions

- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-03-27 - Committee: Committee on Foreign Relations. Ordered to be reported without amendment favorably.
- 2025-04-28 - Committee: Committee on Foreign Relations. Reported by Senator Risch without amendment. Without written report.
- 2025-04-28 - Committee: Committee on Foreign Relations. Reported by Senator Risch without amendment. Without written report.
- 2025-04-28 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 54.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/860",
    "number": "860",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "R000584",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Risch, James E. [R-ID]",
        "lastName": "Risch",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "BUST FENTANYL Act",
    "type": "S",
    "updateDate": "2026-02-24T14:10:39Z",
    "updateDateIncludingText": "2026-02-24T14:10:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-28",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 54.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-04-28",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-04-28",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-27",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-05",
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
        "item": [
          {
            "date": "2025-04-28T20:47:09Z",
            "name": "Reported By"
          },
          {
            "date": "2025-03-27T17:55:17Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-05T17:46:17Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "NH"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "TN"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s860is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 860\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2025 Mr. Risch (for himself and Mrs. Shaheen ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo modify the information about countries exporting methamphetamine that is included in the annual International Narcotics Control Strategy Report, to require a report to Congress on the seizure and production of certain illicit drugs, to impose sanctions with respect to the production and trafficking into the United States, of synthetic opioids, and for other purposes.\n#### 1. Short titles\nThis Act may be cited as the Break Up Suspicious Transactions of Fentanyl Act or the BUST FENTANYL Act .\n#### 2. International Narcotics Control Strategy Report\nSection 489(a) of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2291h(a) ) is amended\u2014\n**(1)**\nin the matter preceding paragraph (1), by striking March 1 and inserting June 1 ; and\n**(2)**\nin paragraph (8)(A)(i), by striking pseudoephedrine and all that follows through chemicals) and inserting chemical precursors used in the production of methamphetamine that significantly affected the United States .\n#### 3. Study and report on efforts to address fentanyl trafficking from the People's Republic of China and other relevant countries\n##### (a) Definitions\nIn this section:\n**(1) Appropriate committees of congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on the Judiciary of the Senate ;\n**(B)**\nthe Committee on Foreign Relations of the Senate ;\n**(C)**\nthe Committee on the Judiciary of the House of Representatives ; and\n**(D)**\nthe Committee on Foreign Affairs of the House of Representatives .\n**(2) DEA**\nThe term DEA means the Drug Enforcement Administration.\n**(3) PRC**\nThe term PRC means the People\u2019s Republic of China.\n##### (b) Study and report on addressing trafficking of fentanyl and other synthetic opioids from the PRC and other relevant countries\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State and the Attorney General shall jointly submit to the appropriate committees of Congress an unclassified written report, with a classified annex, that includes\u2014\n**(1)**\na description of United States Government efforts to gain a commitment from the Government of the PRC to submit unregulated fentanyl precursors, such as 4\u2013AP, to controls;\n**(2)**\na plan for future steps the United States Government will take to urge the Government of the PRC to combat the production and trafficking of illicit fentanyl and synthetic opioids from the PRC, including the trafficking of precursor chemicals used to produce illicit narcotics in Mexico and in other countries;\n**(3)**\na detailed description of cooperation by the Government of the PRC to address the role of the PRC financial system and PRC money laundering organizations in the trafficking of fentanyl and synthetic opioid precursors;\n**(4)**\nan assessment of the expected impact that the designation of principal corporate officers of PRC financial institutions for facilitating narcotics-related money laundering would have on PRC money laundering organizations;\n**(5)**\nan assessment of whether the Trilateral Fentanyl Committee, which was established by the United States, Canada, and Mexico during the January 2023 North American Leaders' Summit, is improving cooperation with law enforcement and financial regulators in Canada and Mexico to combat the role of PRC financial institutions and PRC money laundering organizations in narcotics trafficking;\n**(6)**\nan assessment of the effectiveness of other United States bilateral and multilateral efforts to strengthen international cooperation to address the PRC\u2019s role in the trafficking of fentanyl and synthetic opioid precursors, including through the Global Coalition to Address Synthetic Drug Threats;\n**(7)**\nan update on the status of commitments made by third countries through the Global Coalition to Address Synthetic Drug Threats to combat the synthetic opioid crisis and progress towards the implementation of such commitments;\n**(8)**\na plan for future steps to further strengthen bilateral and multilateral efforts to urge the Government of the PRC to take additional actions to address the PRC\u2019s role in the trafficking of fentanyl and synthetic opioid precursors, particularly in coordination with countries in East Asia and Southeast Asia that have been impacted by such activities;\n**(9)**\nan assessment of how actions the Government of the PRC has taken since November 15, 2023 has shifted relevant supply chains for fentanyl and synthetic opioid precursors, if at all; and\n**(10)**\nthe items described in paragraphs (1) through (4) pertaining to India, Mexico, and other countries the Secretary of State determines to have a significant role in the production or trafficking of fentanyl and synthetic opioid precursors for purposes of this report.\n##### (c) Establishment of DEA offices in the PRC\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State and the Attorney General shall jointly provide to the appropriate committees of Congress a classified briefing on\u2014\n**(1)**\noutreach and negotiations undertaken by the United States Government with the Government of the PRC that was aimed at securing the approval of the Government of the PRC to establish of United States Drug Enforcement Administration offices in Shanghai and Guangzhou, the PRC; and\n**(2)**\nadditional efforts to establish new partnerships with provincial-level authorities in the PRC to counter the illicit trafficking of fentanyl, fentanyl analogues, and their precursors.\n#### 4. Prioritization of identification of persons from the People's Republic of China\nSection 7211 of the Fentanyl Sanctions Act ( 21 U.S.C. 2311 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby redesignating paragraphs (3) and (4) as paragraphs (4) and (5), respectively; and\n**(B)**\nby inserting after paragraph (2) the following:\n(3) Prioritization (A) Defined term In this paragraph, the term person of the People's Republic of China means\u2014 (i) an individual who is a citizen or national of the People's Republic of China; or (ii) an entity organized under the laws of the People's Republic of China or otherwise subject to the jurisdiction of the Government of the People's Republic of China. (B) In general In preparing the report required under paragraph (1), the President shall prioritize, to the greatest extent practicable, the identification of persons of the People's Republic of China involved in the shipment of fentanyl, fentanyl analogues, fentanyl precursors, precursors for fentanyl analogues, pre-precursors for fentanyl and fentanyl analogues, and equipment for the manufacturing of fentanyl and fentanyl-laced counterfeit pills to Mexico or any other country that is involved in the production of fentanyl trafficked into the United States, including\u2014 (i) any entity involved in the production of pharmaceuticals; and (ii) any person that is acting on behalf of any such entity. (C) Termination of prioritization The President shall continue the prioritization required under subparagraph (B) until the President certifies to the appropriate congressional committees that the People\u2019s Republic of China is no longer the primary source for the shipment of fentanyl, fentanyl analogues, fentanyl precursors, precursors for fentanyl analogues, pre-precursors for fentanyl and fentanyl analogues, and equipment for the manufacturing of fentanyl and fentanyl-laced counterfeit pills to Mexico or any other country that is involved in the production of fentanyl trafficked into the United States. ; and\n**(2)**\nin subsection (c), by striking the date that is 5 years after such date of enactment and inserting December 31, 2030 .\n#### 5. Expansion of sanctions under the Fentanyl Sanctions Act\nSection 7212 of the Fentanyl Sanctions Act ( 21 U.S.C. 2312 ) is amended\u2014\n**(1)**\nin paragraph (1), by striking or at the end;\n**(2)**\nin paragraph (2), by striking the period at the end and inserting a semicolon; and\n**(3)**\nby adding at the end the following:\n(3) the President determines has knowingly engaged in, on or after the date of the enactment of the BUST FENTANYL Act , a significant activity or significant financial transaction that has materially contributed to opioid trafficking; or (4) the President determines\u2014 (A) has received any property or interest in property that the foreign person knows\u2014 (i) constitutes or is derived from the proceeds of an activity or transaction described in paragraph (3); or (ii) was used or intended to be used to commit or to facilitate such an activity or transaction; (B) has knowingly provided significant financial, material, or technological support for, including through the provision of goods or services in support of\u2014 (i) any activity or transaction described in paragraph (3); or (ii) any foreign person described in paragraph (3); or (C) is or has been owned, controlled, or directed by any foreign person described in subparagraph (A) or (B) or in paragraph (3), or has knowingly acted or purported to act for or on behalf of, directly or indirectly, such a foreign person. .\n#### 6. Imposition of sanctions with respect to agencies or instrumentalities of foreign states\n##### (a) Definitions\nIn this section, the terms knowingly and opioid trafficking have the meanings given such terms in section 7203 of the Fentanyl Sanctions Act ( 21 U.S.C. 2302 ).\n##### (b) In general\nThe President may\u2014\n**(1)**\nimpose one or more of the sanctions described in section 7213 of the Fentanyl Sanctions Act ( 21 U.S.C. 2313 ) with respect to each political subdivision, agency, or instrumentality of a foreign government, including any financial institution owned or controlled by a foreign government, that the President determines has knowingly, on or after the date of the enactment of this Act\u2014\n**(A)**\nengaged in a significant activity or a significant financial transaction that has materially contributed to opioid trafficking; or\n**(B)**\nprovided financial, material, or technological support for (including through the provision of goods or services in support of) any significant activity or significant financial transaction described in subparagraph (A); and\n**(2)**\nimpose one or more of the sanctions described in section 7213(a)(6) of the Fentanyl Sanctions Act ( 21 U.S.C. 2313(a)(6) ) with respect to each senior official of a political subdivision, agency, or instrumentality of a foreign government that the President determines has knowingly, on or after the date of the enactment of this Act, facilitated a significant activity or a significant financial transaction described in paragraph (1).\n#### 7. Annual report on efforts to prevent the smuggling of methamphetamine into the United States from Mexico\nSection 723(c) of the Combat Methamphetamine Epidemic Act of 2005 ( 22 U.S.C. 2291 note) is amended by striking the period at the end and inserting the following \u201c, which shall\u2014\n(1) identify the significant source countries for methamphetamine that significantly affect the United States, and (2) describe the actions by the governments of the countries identified pursuant to paragraph (1) to combat the diversion of relevant precursor chemicals and the production and trafficking of methamphetamine. .",
      "versionDate": "2025-03-05",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s860rs.xml",
      "text": "II\nCalendar No. 54\n119th CONGRESS\n1st Session\nS. 860\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2025 Mr. Risch (for himself, Mrs. Shaheen , Mr. Hagerty , and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nApril 28, 2025 Reported by Mr. Risch , without amendment\nA BILL\nTo modify the information about countries exporting methamphetamine that is included in the annual International Narcotics Control Strategy Report, to require a report to Congress on the seizure and production of certain illicit drugs, to impose sanctions with respect to the production and trafficking into the United States, of synthetic opioids, and for other purposes.\n#### 1. Short titles\nThis Act may be cited as the Break Up Suspicious Transactions of Fentanyl Act or the BUST FENTANYL Act .\n#### 2. International Narcotics Control Strategy Report\nSection 489(a) of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2291h(a) ) is amended\u2014\n**(1)**\nin the matter preceding paragraph (1), by striking March 1 and inserting June 1 ; and\n**(2)**\nin paragraph (8)(A)(i), by striking pseudoephedrine and all that follows through chemicals) and inserting chemical precursors used in the production of methamphetamine that significantly affected the United States .\n#### 3. Study and report on efforts to address fentanyl trafficking from the People's Republic of China and other relevant countries\n##### (a) Definitions\nIn this section:\n**(1) Appropriate committees of congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on the Judiciary of the Senate ;\n**(B)**\nthe Committee on Foreign Relations of the Senate ;\n**(C)**\nthe Committee on the Judiciary of the House of Representatives ; and\n**(D)**\nthe Committee on Foreign Affairs of the House of Representatives .\n**(2) DEA**\nThe term DEA means the Drug Enforcement Administration.\n**(3) PRC**\nThe term PRC means the People\u2019s Republic of China.\n##### (b) Study and report on addressing trafficking of fentanyl and other synthetic opioids from the PRC and other relevant countries\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State and the Attorney General shall jointly submit to the appropriate committees of Congress an unclassified written report, with a classified annex, that includes\u2014\n**(1)**\na description of United States Government efforts to gain a commitment from the Government of the PRC to submit unregulated fentanyl precursors, such as 4\u2013AP, to controls;\n**(2)**\na plan for future steps the United States Government will take to urge the Government of the PRC to combat the production and trafficking of illicit fentanyl and synthetic opioids from the PRC, including the trafficking of precursor chemicals used to produce illicit narcotics in Mexico and in other countries;\n**(3)**\na detailed description of cooperation by the Government of the PRC to address the role of the PRC financial system and PRC money laundering organizations in the trafficking of fentanyl and synthetic opioid precursors;\n**(4)**\nan assessment of the expected impact that the designation of principal corporate officers of PRC financial institutions for facilitating narcotics-related money laundering would have on PRC money laundering organizations;\n**(5)**\nan assessment of whether the Trilateral Fentanyl Committee, which was established by the United States, Canada, and Mexico during the January 2023 North American Leaders' Summit, is improving cooperation with law enforcement and financial regulators in Canada and Mexico to combat the role of PRC financial institutions and PRC money laundering organizations in narcotics trafficking;\n**(6)**\nan assessment of the effectiveness of other United States bilateral and multilateral efforts to strengthen international cooperation to address the PRC\u2019s role in the trafficking of fentanyl and synthetic opioid precursors, including through the Global Coalition to Address Synthetic Drug Threats;\n**(7)**\nan update on the status of commitments made by third countries through the Global Coalition to Address Synthetic Drug Threats to combat the synthetic opioid crisis and progress towards the implementation of such commitments;\n**(8)**\na plan for future steps to further strengthen bilateral and multilateral efforts to urge the Government of the PRC to take additional actions to address the PRC\u2019s role in the trafficking of fentanyl and synthetic opioid precursors, particularly in coordination with countries in East Asia and Southeast Asia that have been impacted by such activities;\n**(9)**\nan assessment of how actions the Government of the PRC has taken since November 15, 2023 has shifted relevant supply chains for fentanyl and synthetic opioid precursors, if at all; and\n**(10)**\nthe items described in paragraphs (1) through (4) pertaining to India, Mexico, and other countries the Secretary of State determines to have a significant role in the production or trafficking of fentanyl and synthetic opioid precursors for purposes of this report.\n##### (c) Establishment of DEA offices in the PRC\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State and the Attorney General shall jointly provide to the appropriate committees of Congress a classified briefing on\u2014\n**(1)**\noutreach and negotiations undertaken by the United States Government with the Government of the PRC that was aimed at securing the approval of the Government of the PRC to establish of United States Drug Enforcement Administration offices in Shanghai and Guangzhou, the PRC; and\n**(2)**\nadditional efforts to establish new partnerships with provincial-level authorities in the PRC to counter the illicit trafficking of fentanyl, fentanyl analogues, and their precursors.\n#### 4. Prioritization of identification of persons from the People's Republic of China\nSection 7211 of the Fentanyl Sanctions Act ( 21 U.S.C. 2311 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby redesignating paragraphs (3) and (4) as paragraphs (4) and (5), respectively; and\n**(B)**\nby inserting after paragraph (2) the following:\n(3) Prioritization (A) Defined term In this paragraph, the term person of the People's Republic of China means\u2014 (i) an individual who is a citizen or national of the People's Republic of China; or (ii) an entity organized under the laws of the People's Republic of China or otherwise subject to the jurisdiction of the Government of the People's Republic of China. (B) In general In preparing the report required under paragraph (1), the President shall prioritize, to the greatest extent practicable, the identification of persons of the People's Republic of China involved in the shipment of fentanyl, fentanyl analogues, fentanyl precursors, precursors for fentanyl analogues, pre-precursors for fentanyl and fentanyl analogues, and equipment for the manufacturing of fentanyl and fentanyl-laced counterfeit pills to Mexico or any other country that is involved in the production of fentanyl trafficked into the United States, including\u2014 (i) any entity involved in the production of pharmaceuticals; and (ii) any person that is acting on behalf of any such entity. (C) Termination of prioritization The President shall continue the prioritization required under subparagraph (B) until the President certifies to the appropriate congressional committees that the People\u2019s Republic of China is no longer the primary source for the shipment of fentanyl, fentanyl analogues, fentanyl precursors, precursors for fentanyl analogues, pre-precursors for fentanyl and fentanyl analogues, and equipment for the manufacturing of fentanyl and fentanyl-laced counterfeit pills to Mexico or any other country that is involved in the production of fentanyl trafficked into the United States. ; and\n**(2)**\nin subsection (c), by striking the date that is 5 years after such date of enactment and inserting December 31, 2030 .\n#### 5. Expansion of sanctions under the Fentanyl Sanctions Act\nSection 7212 of the Fentanyl Sanctions Act ( 21 U.S.C. 2312 ) is amended\u2014\n**(1)**\nin paragraph (1), by striking or at the end;\n**(2)**\nin paragraph (2), by striking the period at the end and inserting a semicolon; and\n**(3)**\nby adding at the end the following:\n(3) the President determines has knowingly engaged in, on or after the date of the enactment of the BUST FENTANYL Act , a significant activity or significant financial transaction that has materially contributed to opioid trafficking; or (4) the President determines\u2014 (A) has received any property or interest in property that the foreign person knows\u2014 (i) constitutes or is derived from the proceeds of an activity or transaction described in paragraph (3); or (ii) was used or intended to be used to commit or to facilitate such an activity or transaction; (B) has knowingly provided significant financial, material, or technological support for, including through the provision of goods or services in support of\u2014 (i) any activity or transaction described in paragraph (3); or (ii) any foreign person described in paragraph (3); or (C) is or has been owned, controlled, or directed by any foreign person described in subparagraph (A) or (B) or in paragraph (3), or has knowingly acted or purported to act for or on behalf of, directly or indirectly, such a foreign person. .\n#### 6. Imposition of sanctions with respect to agencies or instrumentalities of foreign states\n##### (a) Definitions\nIn this section, the terms knowingly and opioid trafficking have the meanings given such terms in section 7203 of the Fentanyl Sanctions Act ( 21 U.S.C. 2302 ).\n##### (b) In general\nThe President may\u2014\n**(1)**\nimpose one or more of the sanctions described in section 7213 of the Fentanyl Sanctions Act ( 21 U.S.C. 2313 ) with respect to each political subdivision, agency, or instrumentality of a foreign government, including any financial institution owned or controlled by a foreign government, that the President determines has knowingly, on or after the date of the enactment of this Act\u2014\n**(A)**\nengaged in a significant activity or a significant financial transaction that has materially contributed to opioid trafficking; or\n**(B)**\nprovided financial, material, or technological support for (including through the provision of goods or services in support of) any significant activity or significant financial transaction described in subparagraph (A); and\n**(2)**\nimpose one or more of the sanctions described in section 7213(a)(6) of the Fentanyl Sanctions Act ( 21 U.S.C. 2313(a)(6) ) with respect to each senior official of a political subdivision, agency, or instrumentality of a foreign government that the President determines has knowingly, on or after the date of the enactment of this Act, facilitated a significant activity or a significant financial transaction described in paragraph (1).\n#### 7. Annual report on efforts to prevent the smuggling of methamphetamine into the United States from Mexico\nSection 723(c) of the Combat Methamphetamine Epidemic Act of 2005 ( 22 U.S.C. 2291 note) is amended by striking the period at the end and inserting the following \", which shall\u2014\n(1) identify the significant source countries for methamphetamine that significantly affect the United States, and (2) describe the actions by the governments of the countries identified pursuant to paragraph (1) to combat the diversion of relevant precursor chemicals and the production and trafficking of methamphetamine. .",
      "versionDate": "2025-04-28",
      "versionType": "Reported in Senate"
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
        "actionDate": "2025-12-18",
        "text": "Became Public Law No: 119-60."
      },
      "number": "1071",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National Defense Authorization Act for Fiscal Year 2026",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Asia",
            "updateDate": "2025-06-10T17:41:45Z"
          },
          {
            "name": "China",
            "updateDate": "2025-06-10T17:41:38Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-10T17:41:32Z"
          },
          {
            "name": "Department of Justice",
            "updateDate": "2025-06-10T17:42:22Z"
          },
          {
            "name": "Drug trafficking and controlled substances",
            "updateDate": "2025-06-10T17:41:10Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-06-10T17:42:28Z"
          },
          {
            "name": "Foreign and international banking",
            "updateDate": "2025-06-10T17:42:54Z"
          },
          {
            "name": "Foreign property",
            "updateDate": "2025-06-10T17:42:46Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2025-06-10T17:41:51Z"
          },
          {
            "name": "International organizations and cooperation",
            "updateDate": "2025-06-10T17:42:13Z"
          },
          {
            "name": "Latin America",
            "updateDate": "2025-06-10T17:42:05Z"
          },
          {
            "name": "Mexico",
            "updateDate": "2025-06-10T17:41:59Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-06-10T17:42:35Z"
          },
          {
            "name": "Sanctions",
            "updateDate": "2025-06-10T17:41:17Z"
          },
          {
            "name": "Smuggling and trafficking",
            "updateDate": "2025-06-10T17:41:24Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-05-15T12:31:18Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-05",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s860",
          "measure-number": "860",
          "measure-type": "s",
          "orig-publish-date": "2025-03-05",
          "originChamber": "SENATE",
          "update-date": "2026-02-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s860v00",
            "update-date": "2026-02-24"
          },
          "action-date": "2025-03-05",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Break Up Suspicious Transactions of Fentanyl Act or the BUST\u00a0FENTANYL Act</strong></p><p>This bill revives a requirement for the President to identify foreign opioid traffickers and extends opioid trafficking sanctions to new categories of foreign persons (individuals and entities) whose actions support such trafficking.\u00a0</p><p>Specifically, the bill revives through 2030 a requirement that the President annually submit a report to Congress identifying foreign opioid traffickers. (For those listed in the report, the President must select certain sanctions to impose on them, such as bans on loans, foreign exchange transactions, and property transactions.) The bill also specifies that such reports must prioritize the identification of Chinese nationals and entities involved in the shipment of\u00a0fentanyl, fentanyl-related chemicals, and fentanyl manufacturing equipment to Mexico or any other country involved in the production of\u00a0fentanyl trafficked to the United States.</p><p>The bill extends such foreign opioid trafficker sanctions to additional categories of foreign persons, including those that have knowingly (1) engaged in significant activities or financial transactions that materially contributed to opioid trafficking; or (2) provided financial, material, or technological support for such activities or transactions.</p><p>The bill also authorizes the President to impose these sanctions on foreign government entities, including government owned or controlled financial institutions, that are involved in activities that contribute to opioid trafficking. Additionally, the President may impose property-blocking sanctions on senior officials of these foreign government entities who knowingly facilitate such\u00a0activities.</p>"
        },
        "title": "BUST FENTANYL Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s860.xml",
    "summary": {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Break Up Suspicious Transactions of Fentanyl Act or the BUST\u00a0FENTANYL Act</strong></p><p>This bill revives a requirement for the President to identify foreign opioid traffickers and extends opioid trafficking sanctions to new categories of foreign persons (individuals and entities) whose actions support such trafficking.\u00a0</p><p>Specifically, the bill revives through 2030 a requirement that the President annually submit a report to Congress identifying foreign opioid traffickers. (For those listed in the report, the President must select certain sanctions to impose on them, such as bans on loans, foreign exchange transactions, and property transactions.) The bill also specifies that such reports must prioritize the identification of Chinese nationals and entities involved in the shipment of\u00a0fentanyl, fentanyl-related chemicals, and fentanyl manufacturing equipment to Mexico or any other country involved in the production of\u00a0fentanyl trafficked to the United States.</p><p>The bill extends such foreign opioid trafficker sanctions to additional categories of foreign persons, including those that have knowingly (1) engaged in significant activities or financial transactions that materially contributed to opioid trafficking; or (2) provided financial, material, or technological support for such activities or transactions.</p><p>The bill also authorizes the President to impose these sanctions on foreign government entities, including government owned or controlled financial institutions, that are involved in activities that contribute to opioid trafficking. Additionally, the President may impose property-blocking sanctions on senior officials of these foreign government entities who knowingly facilitate such\u00a0activities.</p>",
      "updateDate": "2026-02-24",
      "versionCode": "id119s860"
    },
    "title": "BUST FENTANYL Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Break Up Suspicious Transactions of Fentanyl Act or the BUST\u00a0FENTANYL Act</strong></p><p>This bill revives a requirement for the President to identify foreign opioid traffickers and extends opioid trafficking sanctions to new categories of foreign persons (individuals and entities) whose actions support such trafficking.\u00a0</p><p>Specifically, the bill revives through 2030 a requirement that the President annually submit a report to Congress identifying foreign opioid traffickers. (For those listed in the report, the President must select certain sanctions to impose on them, such as bans on loans, foreign exchange transactions, and property transactions.) The bill also specifies that such reports must prioritize the identification of Chinese nationals and entities involved in the shipment of\u00a0fentanyl, fentanyl-related chemicals, and fentanyl manufacturing equipment to Mexico or any other country involved in the production of\u00a0fentanyl trafficked to the United States.</p><p>The bill extends such foreign opioid trafficker sanctions to additional categories of foreign persons, including those that have knowingly (1) engaged in significant activities or financial transactions that materially contributed to opioid trafficking; or (2) provided financial, material, or technological support for such activities or transactions.</p><p>The bill also authorizes the President to impose these sanctions on foreign government entities, including government owned or controlled financial institutions, that are involved in activities that contribute to opioid trafficking. Additionally, the President may impose property-blocking sanctions on senior officials of these foreign government entities who knowingly facilitate such\u00a0activities.</p>",
      "updateDate": "2026-02-24",
      "versionCode": "id119s860"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s860is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s860rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "BUST FENTANYL Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-04-30T04:08:17Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Break Up Suspicious Transactions of Fentanyl Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-04-30T04:08:17Z"
    },
    {
      "title": "BUST FENTANYL Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-29T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "BUST FENTANYL Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Break Up Suspicious Transactions of Fentanyl Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to modify the information about countries exporting methamphetamine that is included in the annual International Narcotics Control Strategy Report, to require a report to Congress on the seizure and production of certain illicit drugs, to impose sanctions with respect to the production and trafficking into the United States, of synthetic opioids, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T03:18:49Z"
    }
  ]
}
```
