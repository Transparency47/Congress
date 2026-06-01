# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8740?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8740
- Title: Iranian Temporary Immigration Relief Act
- Congress: 119
- Bill type: HR
- Bill number: 8740
- Origin chamber: House
- Introduced date: 2026-05-12
- Update date: 2026-05-30T09:23:27Z
- Update date including text: 2026-05-30T09:23:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, text, titles

## Timeline

- 2026-05-12: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-05-12: Introduced in House

## Actions

- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-12",
    "latestAction": {
      "actionDate": "2026-05-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8740",
    "number": "8740",
    "originChamber": "House",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "A000381",
        "district": "3",
        "firstName": "Yassamin",
        "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
        "lastName": "Ansari",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "Iranian Temporary Immigration Relief Act",
    "type": "HR",
    "updateDate": "2026-05-30T09:23:27Z",
    "updateDateIncludingText": "2026-05-30T09:23:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-12",
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
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-12",
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
          "date": "2026-05-12T16:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "NY"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "CA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "CO"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8740ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8740\nIN THE HOUSE OF REPRESENTATIVES\nMay 12, 2026 Ms. Ansari (for herself and Mr. Suozzi ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo provide temporary protected status and employment authorization to certain Iranian nationals adversely affected by the adjudication pause of December 2025, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Iranian Temporary Immigration Relief Act .\n#### 2. Findings\nThe Congress finds the following:\n**(1)**\nSince early 2026, the United States has been engaged in armed hostilities with the Islamic Republic of Iran, including direct military strikes on Iranian territory, naval confrontations in the Persian Gulf, and sustained operations targeting Iranian military and nuclear infrastructure. These hostilities have resulted in significant civilian casualties, displacement of Iranian populations, and a severe deterioration of security conditions throughout the Islamic Republic of Iran.\n**(2)**\nThe state of conflict between the United States and Iran has created extraordinary and temporary conditions in Iran within the meaning of section 244(b)(1)(C) of the Immigration and Nationality Act ( 8 U.S.C. 1254a(b)(1)(C) ), including but not limited to: destruction of civilian infrastructure; disruption of essential services including healthcare, transportation, and communications; economic instability driven by internal mismanagement, conflict, and broader economic disruption; and a pervasive climate of danger to any individual perceived by the Iranian regime as having ties to the United States, such that Iranian nationals in the United States cannot safely return to Iran, and their return would pose a serious threat to their personal safety.\n**(3)**\nIndependent of and compounding the conditions created by the armed conflict, the Iranian regime has engaged in a campaign of widespread atrocities against its own civilian population, including massacres of civilians in January 2026 and the months following, mass arrests of political dissidents and perceived opponents, extrajudicial killings, enforced disappearances, systematic use of torture in detention facilities, the violent suppression of public dissent, a near-total nationwide internet shutdown. These acts of state repression constitute additional extraordinary and temporary conditions within the meaning of section 244(b)(1)(C) of the Immigration and Nationality Act ( 8 U.S.C. 1254a(b)(1)(C) ) and create a pervasive climate of danger to any individual perceived by the Iranian regime as having ties to the United States, opposition sympathies, or connections to the Iranian diaspora.\n**(4)**\nThe Government of the Islamic Republic of Iran is distinct from the Iranian people, many of whom oppose the regime and would face heightened risk of persecution if returned.\n**(5)**\nIn December 2025, U.S. Citizenship and Immigration Services implemented a pause on the adjudication of benefit applications filed by nationals of Iran, in connection with national security concerns involving the Islamic Republic of Iran.\n**(6)**\nThe adjudication pause has caused significant and specific harm to Iranian nationals lawfully present in the United States who have pending applications for change of nonimmigrant or immigrant status, extension of stay, or employment authorization that were filed in good faith and in compliance with applicable law.\n**(7)**\nCertain Iranian nationals whose underlying immigration status may expire during the adjudication pause are now in a state of legal limbo\u2014their lawful presence depends solely on the continued pendency of applications that USCIS has paused to adjudicate, exposing them to potential accrual of unlawful presence, removal proceedings, and inadmissibility consequences through no fault of their own.\n**(8)**\nCertain Iranian nationals whose employment authorization documents may expire during the adjudication pause, and whose timely filed renewal applications remain unadjudicated, are unable to lawfully work, causing severe financial hardship to them and their families.\n**(9)**\nThese individuals took all steps required by law to maintain their immigration status and work authorization, and their current predicament is the direct result of government action rather than any failure on their part.\n**(10)**\nIranian nationals who have resided in the United States face a heightened and particularized risk of persecution, detention, interrogation, or violence at the hands of the Iranian government and its affiliated security forces upon return to Iran, based on their perceived association with the United States, their exposure to Western society, and the Iranian regime\u2019s documented pattern of retaliating against individuals with American connections during periods of bilateral hostility.\n**(11)**\nMany of the Iranian nationals affected by the adjudication pause have, in the months preceding and following the onset of hostilities, actively and publicly participated in pro-democracy demonstrations against the Islamic Republic of Iran within the United States, and have engaged in online advocacy campaigns\u2014including on social media platforms widely monitored by Iranian intelligence services\u2014in support of the Iranian people\u2019s aspirations for freedom, human rights, and democratic governance. These individuals face a particularly acute and well-documented risk of persecution, imprisonment, torture, or execution by the Iranian regime should they be compelled to return to Iran, as the regime has a systematic and well-documented practice of identifying, tracking, and retaliating against diaspora activists and their family members inside Iran.\n**(12)**\nAmong the Iranian nationals adversely affected by the adjudication pause are engineers, physicians, biomedical researchers, technology entrepreneurs, academic scientists, and other highly skilled professionals who have made substantial contributions to the United States economy, to American innovation and competitiveness, and to sectors of critical national importance including healthcare, artificial intelligence, technology, and advanced manufacturing. The United States has historically benefitted enormously from the talents of Iranian-born professionals\u2014who are among the most highly educated immigrant populations in the country\u2014and the loss of their labor, expertise, and entrepreneurial activity due to the adjudication pause causes measurable harm to American economic output, scientific advancement, and national competitiveness.\n**(13)**\nThe combination of armed hostilities with Iran and the adjudication pause has created an unprecedented situation in which Iranian nationals in the United States are simultaneously unable to return safely to their home country due to war, unable to maintain or obtain lawful immigration status due to the United States Government\u2019s refusal to adjudicate their applications, and unable to work lawfully to support themselves and their families\u2014a convergence of harms that demands targeted legislative relief.\n**(14)**\nIt is in the national interest of the United States to provide temporary protection and work authorization to these individuals to prevent unjust hardship, maintain economic productivity, uphold the integrity of the immigration system by ensuring that individuals who comply with the law are not penalized for government-caused delays, and to demonstrate that the United States distinguishes between the Iranian people\u2014many of whom oppose the Iranian regime\u2014and the Government of the Islamic Republic of Iran with which the United States is in conflict.\n#### 3. Definitions\nIn this Act:\n**(1) Adjudication pause**\nThe term adjudication pause means any suspension, hold, delay, or de facto cessation of the adjudication by U.S. Citizenship and Immigration Services of benefit applications filed by nationals of Iran that was initiated on or after December 1, 2025, whether pursuant to executive order, presidential proclamation, agency policy memorandum, or other directive.\n**(2) Benefit application**\nThe term benefit application means\u2014\n**(A)**\nan application for change of nonimmigrant classification under section 248 of the Immigration and Nationality Act ( 8 U.S.C. 1258 ), for extension of stay, or for adjustment of status under section 245 of such Act ( 8 U.S.C. 1255 ); and\n**(B)**\nan application for employment authorization or for renewal of an employment authorization document under section 274A(h)(3) of the Immigration and Nationality Act ( 8 U.S.C. 1324a(h)(3) ) and the regulations promulgated thereunder.\n**(3) Eligible individual**\nThe term eligible individual means an individual who\u2014\n**(A)**\nis a national of Iran;\n**(B)**\nwas lawfully admitted to the United States or otherwise lawfully present;\n**(C)**\nfiled, prior to or during the adjudication pause, a benefit application, that was not adjudicated due, in whole or in part, to the adjudication pause; and\n**(D)**\nhas\u2014\n**(i)**\na nonimmigrant status or an authorized period of stay that has expired or will expire during the period of the adjudication pause, such that the alien\u2019s continued lawful presence depends on the pendency of the unadjudicated benefit application; or\n**(ii)**\nan employment authorization\u2014\n**(I)**\nthat has expired or will expire during the period of the adjudication pause; and\n**(II)**\nwith respect to which any applicable automatic extension period under section 274a.13(d) of title 8, Code of Federal Regulations (or any successor regulation), has expired or will expire before the adjudication pause is terminated or the benefit application is adjudicated.\n**(4) Secretary**\nThe term Secretary means the Secretary of Homeland Security.\n#### 4. Designation of temporary protected status for eligible Iranian nationals\n##### (a) Designation\nNotwithstanding any other provision of law, for the purpose of section 244 of the Immigration and Nationality Act ( 8 U.S.C. 1254a ), Iran shall be treated as if it had been designated under subsection (b)(1)(C) of that section, subject to the provisions of this section.\n##### (b) Duration\n**(1) In general**\nThe initial designation under subsection (a) shall be in effect for a period of 18 months beginning on the date of enactment of this Act.\n**(2) Extension**\nThe Secretary shall extend the designation under subsection (a) for additional periods of 6 months each if the Secretary determines, at least 60 days before the end of the current designation period, that\u2014\n**(A)**\nthe adjudication pause remains in effect, in whole or in part; or\n**(B)**\nthe conditions that gave rise to the adjudication pause continue to exist such that eligible individuals cannot reasonably expect timely adjudication of their pending applications.\n**(3) Mandatory extension**\nIf the Secretary fails to make the determination described in paragraph (2) at least 60 days before the end of the current designation period, the designation shall be automatically extended for 6 months.\n##### (c) Scope\nThe designation under this section shall apply exclusively to eligible individuals. Nothing in this section shall be construed to create a designation for all nationals of Iran.\n#### 5. Eligibility and application\n##### (a) Eligibility individuals\nAn alien may be granted temporary protected status in accordance with this Act if the alien\u2014\n**(1)**\nis an eligible individual;\n**(2)**\nis physically present in the United States on the date of enactment of this Act;\n**(3)**\nhas been continuously physically present in the United States since December 2, 2025;\n**(4)**\nis not inadmissible under section 212(a) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a) );\n**(5)**\nhas not been convicted of any felony or 2 or more misdemeanors committed in the United States;\n**(6)**\nis not described in section 208(b)(2)(A) of the Immigration and Nationality Act ( 8 U.S.C. 1158(b)(2)(A) ) (relating to persecution of others, conviction of particularly serious crimes, commission of serious nonpolitical crimes, or danger to the security of the United States); and\n**(7)**\nis not an alien whom the adjudicating officer or the Secretary knows or has reasonable grounds to believe\u2014\n**(A)**\nis or has been an official or agent of the Government of the Islamic Republic of Iran, the Islamic Revolutionary Guard Corps, or any entity owned or controlled by the foregoing, who has been responsible for or complicit in, or has directly or indirectly ordered, controlled, or otherwise directed\u2014\n**(i)**\nacts of corruption, including corruption related to the extraction, sale, or significant diversion of natural resources or public funds;\n**(ii)**\ngross violations of internationally recognized human rights, including torture, extrajudicial killing, prolonged arbitrary detention, enforced disappearance, or systematic repression of the rights to freedom of expression, assembly, or association; or\n**(iii)**\nthe provision of material support, financing, or significant services to the Government of the Islamic Republic of Iran, the Islamic Revolutionary Guard Corps, or any person or entity that is the subject of sanctions or designation under Executive Order 13553, Executive Order 13846, the Iran Threat Reduction and Syria Human Rights Act of 2012, or any other provision of United States law relating to Iran; or\n**(B)**\nis an immediate family member of an alien described in subparagraph (A) who has knowingly obtained, or who reasonably should have known that they were obtaining, any financial benefit or other material advantage derived from the illicit activity of that alien described in subparagraph (A).\n##### (b) Application\n**(1) Commencement of adjudication**\nNot later than 30 days after the date of enactment of this Act, the Secretary shall commence the adjudication of applications for temporary protected status filed in accordance with this Act.\n**(2) Timing of adjudications**\nThe Secretary shall adjudicate any application filed in accordance with this Act not later than 90 days after receipt of such application.\n**(3) Fee**\nThe fee for an application filed in accordance with this section shall not exceed the fee charged for an application for temporary protected status under section 244 of the Immigration and Nationality Act ( 8 U.S.C. 1254a ).\n##### (c) Waiver of grounds of ineligibility\nIn determining an alien\u2019s eligibility under this section, the Secretary may waive any ground of ineligibility under subsection (a).\n#### 6. Employment authorization\n##### (a) In general\nThe Secretary shall authorize an alien granted temporary protected status under section 244 of the Immigration and Nationality Act ( 8 U.S.C. 1254a ) in accordance with this Act to engage in employment in the United States and shall provide such alien with an employment authorization document.\n##### (b) Timing\n**(1) Interim employment authorization**\nNot later than 30 days after an eligible individual files an application for temporary protected status, the Secretary shall issue an interim employment authorization document valid for a period of 180 days, unless the Secretary determines within such 30-day period that the applicant is ineligible.\n**(2) Final employment authorization**\nUpon granting temporary protected status, the Secretary shall issue an employment authorization document valid for the duration of the designation under section 4.\n##### (c) Automatic extension of existing EAD\nFor any eligible individual who has a pending benefit application for an employment authorization that is subject to the adjudication pause, the automatic extension period under section 274a.13(d) of title 8, Code of Federal Regulations, shall be extended for an additional period equal to the duration of the adjudication pause, plus 180 days.\n##### (d) No gap in work authorization\nFor purposes of any Federal or State law, regulation, or policy, an eligible individual who is granted temporary protected status in accordance with this Act shall be deemed to have been continuously authorized for employment from the date on which the individual\u2019s prior employment authorization expired due to the adjudication pause through the date on which employment authorization is issued under this section. No employer shall be liable under section 274A of the Immigration and Nationality Act ( 8 U.S.C. 1324a ) for employing such individual during such gap period.\n#### 7. Protection of pending applications and status\n##### (a) No prejudice\nThe filing for, receipt of, or grant of temporary protected status in accordance with this Act shall not\u2014\n**(1)**\nbe considered a negative factor or adverse evidence in the adjudication of any pending or future application for change of nonimmigrant classification, extension of stay, adjustment of status, employment authorization, or any other immigration benefit;\n**(2)**\nconstitute an abandonment of any pending application for any immigration benefit;\n**(3)**\naffect the priority date, processing date, or queue position of any pending application; or\n**(4)**\nbe used as a basis for initiating removal proceedings or for any enforcement action.\n##### (b) Protection against unlawful presence\nNo period during which an eligible individual has temporary protected status under this Act, or during which the individual\u2019s application for such status is pending, shall be considered a period of unlawful presence under section 212(a)(9)(B) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(9)(B) ).\n##### (c) Protection against accrual during pause\nNotwithstanding any other provision of law, no period during which an eligible individual\u2019s application was pending and subject to the adjudication pause shall be considered a period of unlawful presence for purposes of any provision of the Immigration and Nationality Act, regardless of whether the individual is granted temporary protected status under this Act.\n##### (d) Travel authorization\nThe Secretary shall establish a process by which individuals granted temporary protected status in accordance with this Act may apply for advance parole for travel outside the United States. Such travel shall not constitute an abandonment of any pending application for change of status, adjustment of status, or other immigration benefit.\n#### 8. Reporting\nNot later than 90 days after the date of enactment of this Act, and every 90 days thereafter until all applications subject to the adjudication pause have been adjudicated, the Secretary shall submit to the Committee on the Judiciary of the House of Representatives and the Committee on the Judiciary of the Senate a report that includes\u2014\n**(1)**\nthe total number of applications subject to the adjudication pause, disaggregated by application type;\n**(2)**\nthe number of applications adjudicated during the reporting period;\n**(3)**\nthe number of adjudication applications approved, denied, and pending;\n**(4)**\nthe average processing time for adjudicated applications;\n**(5)**\nthe total number of applications for temporary protected status filed in accordance with this Act during the reporting period, and the cumulative total since the date of enactment;\n**(6)**\nthe number of applications for temporary protected status approved during the reporting period, and the cumulative total since the date of enactment; and\n**(7)**\nthe number of applications for temporary protected status denied during the reporting period, disaggregated by the basis for denial, including the number denied on national security grounds under section 5(a)(6), the number denied on public safety grounds under section 5(a)(5), and the number denied on all other grounds, together with a description of the categories of such other grounds.\n#### 9. Rulemaking\n##### (a) Interim final rule\nNot later than 30 days after the date of enactment of this Act, the Secretary shall publish an interim final rule implementing this Act, which shall take effect immediately upon publication.\n##### (b) Final rule\nNot later than 180 days after the date of enactment of this Act, the Secretary shall publish a final rule implementing this Act after providing an opportunity for public comment on the interim final rule.",
      "versionDate": "2026-05-12",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8740ih.xml"
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
      "title": "Iranian Temporary Immigration Relief Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-30T09:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Iranian Temporary Immigration Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-30T09:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide temporary protected status and employment authorization to certain Iranian nationals adversely affected by the adjudication pause of December 2025, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-30T09:18:26Z"
    }
  ]
}
```
