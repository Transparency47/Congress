# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1542?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1542
- Title: Uyghur Policy Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1542
- Origin chamber: Senate
- Introduced date: 2025-04-30
- Update date: 2026-03-18T11:03:17Z
- Update date including text: 2026-03-18T11:03:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-30: Introduced in Senate
- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-04-30: Introduced in Senate

## Actions

- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1542",
    "number": "1542",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "C001114",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Curtis, John R. [R-UT]",
        "lastName": "Curtis",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Uyghur Policy Act of 2025",
    "type": "S",
    "updateDate": "2026-03-18T11:03:17Z",
    "updateDateIncludingText": "2026-03-18T11:03:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-30",
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
      "actionDate": "2025-04-30",
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
            "date": "2025-04-30T20:58:00Z",
            "name": "Referred To"
          },
          {
            "date": "2025-04-30T20:58:00Z",
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
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1542is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1542\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2025 Mr. Curtis introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo support the human rights of Uyghurs and members of other minority groups residing primarily in the Xinjiang Uyghur Autonomous Region, to safeguard their distinct identity, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Uyghur Policy Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe People\u2019s Republic of China (referred to in this Act as the PRC ) continues to repress the distinct Islamic, Turkic identity of Uyghurs and members of other ethnic and religious minority groups in the Xinjiang Uyghur Autonomous Region (referred to in this Act as the XUAR ) in northwestern China and other areas in which they have habitually residided.\n**(2)**\nUyghurs and other predominantly Muslim ethnic minorities historically making up the majority of the XUAR population have maintained a distinct religious and cultural identity throughout their history.\n**(3)**\nHuman rights, including the freedom of religion or belief, and respect for the Uyghurs\u2019 unique Muslim identity are legitimate interests of the international community.\n**(4)**\nThe PRC\u2014\n**(A)**\nhas ratified the International Covenant on Economic, Social and Cultural Rights, done at New York December 16, 1966, and is thereby bound by its provisions; and\n**(B)**\nhas also signed the International Covenant on Civil and Political Rights, done at New York December 19, 1966.\n**(5)**\nAn official campaign to encourage Han Chinese migration into the XUAR has placed immense pressure on Uyghurs and other ethnic and religious minority groups who seek to preserve their unique ethnic, cultural, religious, and linguistic traditions.\n**(6)**\nPRC authorities have supported an influx of Han Chinese economic immigrants into the XUAR, implemented discrimination against Uyghurs and other minorities in hiring practices, and provided unequal access to healthcare services.\n**(7)**\nPRC authorities have manipulated the strategic objectives of the international war on terror to mask their increasing cultural and religious oppression of the Muslim population residing in the XUAR.\n**(8)**\nIn 2014, following unrest in the XUAR, Chinese authorities launched the Strike Hard Against Violent Extremism campaign, in which dubious allegations of widespread extremist activity were used as justification for gross human rights violations committed against Uyghurs and members of other minority communities in the XUAR.\n**(9)**\nPRC authorities have made use of the legal system as a tool of repression, including for the imposition of arbitrary detentions and torture against members of the Uyghur community and other minority populations.\n**(10)**\nUyghurs and Kazakhs who have secured citizenship or permanent residency outside of the PRC have attested to repeated threats, harassment, and surveillance by PRC officials.\n**(11)**\nReporting from international news organizations has found that during the past decade, family members of Uyghurs and other minority groups living outside of the PRC have gone missing or been detained to force Uyghur expatriates to return to the PRC or silence their dissent.\n**(12)**\nIn 2017, Radio Free Asia\u2019s Uyghur Service was the first media organization to report on the PRC\u2019s vast, mass arbitrary-detention program in the XUAR.\n**(13)**\nCredible evidence from human rights organizations, think tanks, and journalists confirms that more than 1,000,000 Uyghurs and members of other ethnic minority groups have been imprisoned in extrajudicial political reeducation centers.\n**(14)**\nIndependent accounts from former detainees of political reeducation centers describe inhumane conditions and treatment including forced political indoctrination, torture, beatings, rape, forced sterilization, and food deprivation.\n**(15)**\nFormer detainees also confirmed that they were told by guards that the only way to secure release was to demonstrate sufficient political loyalty to the Government of the PRC.\n**(16)**\nPopular discourse surrounding the ongoing atrocities in the XUAR and advocacy efforts to assist Uyghurs remains muted in most Muslim majority nations around the world.\n**(17)**\nFormer Secretaries of State Antony Blinken and Michael Pompeo and Secretary of State Marco Rubio have all confirmed that the Government of the PRC has committed genocide and crimes against humanity against Uyghurs and other ethnic and religious minorities in the XUAR.\n**(18)**\nGovernment bodies of multiple countries have also declared that atrocities by the Government of the PRC against such populations in the XUAR constitute genocide, including the Parliament of the United Kingdom, of Belgium, of Czechia, of Lithuania, of the Netherlands, and of Canada.\n#### 3. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe Government of the PRC should immediately open the XUAR to regular, transparent, and unmanipulated visits by\u2014\n**(A)**\nmembers of the press;\n**(B)**\ninternational organizations, including the Office of the United Nations High Commissioner for Human Rights;\n**(C)**\nacademic and human rights research institutions; and\n**(D)**\nforeign delegations, including delegations from the Congress of the United States;\n**(2)**\nthe Government of the PRC should\u2014\n**(A)**\nrecognize, and take tangible steps to protect and preserve, the distinct ethnic, cultural, religious, and linguistic identity of Uyghurs and members of other ethnic and religious minority groups in the XUAR;\n**(B)**\ncease all government-sponsored crackdowns, imprisonments, and detentions of people throughout the XUAR aimed at repressing their ethnic, cultural, political, or religious identities; and\n**(C)**\ncease all government-sponsored transnational repression of Uyghurs, including the detainment, harassment, intimidation, and surveillance of the family members of exiled Uyghurs and Uyghur activists;\n**(3)**\nit is commendable that countries, including Turkey, Albania, and Germany, have provided shelter and hospitality to Uyghurs and other minority group members in exile from the PRC;\n**(4)**\nurges all countries, especially fellow democracies and countries with sizeable Muslim populations, to condemn and address the plight of Uyghurs and other minority communities in the XUAR;\n**(5)**\nthe Government of the PRC should immediately grant unconditional releases to all prisoners that have been detained for their ethnic, cultural, religious, and linguistic identities, for expressing their political or religious beliefs in the XUAR, or for being related to members of the Uyghur diaspora or activist community, including\u2014\n**(A)**\nEkper Asat, who participated in the Department of State\u2019s International Visitors Leadership Program in 2016, was incarcerated after returning to the XUAR, and is now serving a 15-year prison sentence on charges of inciting ethnic hatred and ethnic discrimination ;\n**(B)**\nDr. Gulshan Abbas, a Uyghur retired medical doctor who was wrongfully detained in the XUAR on September 11, 2018, and unjustly sentenced to 20 years in prison in retaliation for her sister\u2019s advocacy for Uyghur human rights issues; and\n**(C)**\nKamile Wayit, a Uyghur university student who was wrongfully detained on December 12, 2022, after returning to the XUAR during the winter holiday while on break from studying;\n**(6)**\nthe Government of the PRC should facilitate access for international humanitarian organizations, including the International Federation of Red Cross and Red Crescent Societies, to the political reeducation centers in the XUAR to ensure prisoners are not being mistreated and are receiving necessary medical care; and\n**(7)**\nthe Department of State should continue to facilitate the unhindered dissemination to the international community of information regarding the human rights, religious freedom, and transnational repression of Uyghurs and members of other minority groups in the XUAR.\n#### 4. United States strengthening of coordination on Uyghur issues\n##### (a) In general\nThe Secretary of State, as appropriate, shall\u2014\n**(1)**\nprioritize policies, programs, and projects to support the Uyghurs and members of other ethnic and religious minority groups in the XUAR;\n**(2)**\nvigorously promote the policies of\u2014\n**(A)**\nprotecting the distinct ethnic, religious, cultural, and linguistic identities of the Uyghurs and other minority groups; and\n**(B)**\nimproving the protection of human rights in the XUAR;\n**(3)**\ndirect the Department of State to maintain close contact with Uyghur religious, cultural, and political leaders, including seeking regular travel to the XUAR and to Uyghur populations in Central Asia, Turkey, Albania, Germany, and other parts of Europe;\n**(4)**\nlead coordination efforts for the release of political prisoners in the XUAR who are being detained for exercising their human rights or being relatives of exiled Uyghurs;\n**(5)**\nconsult with Congress regarding policies relevant to the XUAR and the Uyghurs;\n**(6)**\ncoordinate with relevant Federal agencies to administer aid to Uyghur rights advocates;\n**(7)**\nstrive to establish contacts with foreign ministries of other countries, especially in Europe, Central Asia, and members of the Organisation of Islamic Cooperation, to pursue a policy of promoting greater respect for human rights and religious freedom for Uyghurs and other ethnic and religious minority groups in the XUAR;\n**(8)**\nutilize Strategic Dialogue with the Organisation of Islamic Cooperation to address Uyghur rights and work with its individual member states to develop and implement joint initiatives and programs aimed at promoting awareness of Uyghur rights and supporting Uyghur victims of detainment, harassment, and transnational repression;\n**(9)**\nsupport independent media authorized under section 309 of the United States International Broadcasting Act of 1994 ( 22 U.S.C. 6208 ), including Radio Free Asia, which conduct reporting and investigative journalism focused on the XUAR, including in local languages, to ensure the reporting of future PRC human rights abuses;\n**(10)**\nwork with international partners to raise awareness concerning acts of transnational repression against Uyghur Americans or Uyghurs who are living in exile in the United States and develop and implement strategies to prevent and respond to such transnational repression;\n**(11)**\nestablish a reporting mechanism for individuals to report incidents of transnational repression against Uyghurs and other minority groups with ties to the XUAR; and\n**(12)**\nsubmit to Congress an annual report, including a classified annex, if necessary, that\u2014\n**(A)**\ndescribes actions taken by the United States to address and prevent transnational repression against Uyghurs in the United States; and\n**(B)**\nincludes recommendations for further legislative or policy measures in support of the human rights of Uyghurs and other minority groups from the XUAR.\n##### (b) Support\nThe Secretary of State shall ensure the Department of State has adequate resources, staff, and administrative support to carry out this section.\n##### (c) Sunset\nThe requirements under this section shall cease to have any force or effect beginning on the date that is 5 years after the date of the enactment of this Act.\n#### 5. Funding for human rights advocates to conduct public diplomacy in the Islamic world on the Uyghur situation\n##### (a) In general\nOf the amounts appropriated for the Office of the United States Speaker Program of the Bureau of Educational and Cultural Affairs of the Department of State for each of the fiscal years 2025, 2026, and 2027, $250,000 shall be made available to support human rights advocates working on behalf of the Uyghurs and members of other ethnic and religious minority groups from the XUAR that are being persecuted in the PRC.\n##### (b) Identification of speakers\nThe Assistant Secretary of State for Educational and Cultural Affairs, in consultation with representatives of the global Uyghur community, shall identify human rights advocates who may be invited to speak at global public diplomacy forums, particularly events at which representatives from Organisation of Islamic Cooperation countries and other Muslim-majority countries are present, regarding issues regarding the human rights and religious freedom of Uyghurs and members of other ethnic and religious minority groups who have been persecuted by the PRC.\n#### 6. No additional funds authorized\nNo additional funds are authorized to carry out the requirements under this Act. Such requirements shall be carried out using amounts otherwise authorized for similar purposes.\n#### 7. Access to detention facilities and prisons and the release of prisoners\n##### (a) Strategy on political reeducation and detention facilities\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State, in consultation with the heads of other relevant Federal departments and agencies, shall develop a strategy for cooperating with like-minded partners to pressure the Government of the PRC\u2014\n**(1)**\nto close all detention facilities and political reeducation camps housing Uyghurs and members of other ethnic minority groups in the XUAR;\n**(2)**\nto allow unhindered access to detention facilities and political reeducation camps in the XUAR by independent media, researchers, international organizations and the Office of the United Nations High Commissioner for Human Rights for a comprehensive assessment of the human rights situation; and\n**(3)**\nto protect human rights and preserve the distinct religious and cultural identity of the Uyghurs and the other religious and ethnic minority communities in the XUAR.\n##### (b) Report on strategy and implementation\nNot later than 1 year after the date of the enactment of this Act, the Secretary of State shall submit to the Committee on Foreign Relations of the Senate and the Committee on Foreign Affairs of the House of Representatives a report, including a classified annex, if necessary, that includes\u2014\n**(1)**\nthe strategy developed pursuant to subsection (a); and\n**(2)**\nall of the steps that have been taken to implement such strategy in accordance with the objectives described in paragraphs (1) through (3) of subsection (a).\n#### 8. Requirement for Uyghur language training\n##### (a) Uyghur language training and staffing\nThe Secretary of State shall take such steps as may be necessary to ensure that\u2014\n**(1)**\nUyghur language training is available to Foreign Service officers, as appropriate; and\n**(2)**\nefforts are made to ensure that at least 1 Uyghur-speaking member of the Service (as defined in section 103 of the Foreign Service Act of 1980 ( 22 U.S.C. 3903 )) is assigned to each United States diplomatic or consular post in China.\n##### (b) Report\nNo later than 1 year after the date of the enactment of this Act, and annually thereafter for the following 2 years, the Foreign Service Institute shall submit a report to the Committee on Foreign Relations of the Senate and the Committee on Foreign Affairs of the House of Representatives that outlines all of the steps that have been taken to implement subsection (a).\n#### 9. Uyghur considerations at the United Nations\nThe President should direct the United States Permanent Representative to the United Nations to use the voice, vote, and influence of the United States\u2014\n**(1)**\nto oppose any efforts to prevent consideration of the gross violation of internationally recognized human rights in the XUAR in any body of the United Nations;\n**(2)**\nto oppose any efforts to prevent the participation of any Uyghur human rights advocates in nongovernmental fora hosted by, or otherwise organized under the auspices of, any body of the United Nations; and\n**(3)**\nto support the appointment of a special rapporteur or working group for the XUAR for the purposes of\u2014\n**(A)**\nmonitoring human rights violations and abuses in the XUAR; and\n**(B)**\nmaking reports containing information about such violations and abuses available to the United Nations High Commissioner for Refugees, the United Nations Commission on Human Rights, the General Assembly of the United Nations, and other United Nations subsidiaries.",
      "versionDate": "2025-04-30",
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
        "updateDate": "2025-05-29T12:03:58Z"
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
      "date": "2025-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1542is.xml"
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
      "title": "Uyghur Policy Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Uyghur Policy Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-10T04:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to support the human rights of Uyghurs and members of other minority groups residing primarily in the Xinjiang Uyghur Autonomous Region, to safeguard their distinct identity, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-10T04:33:26Z"
    }
  ]
}
```
