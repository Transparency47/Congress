# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7457?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7457
- Title: Nigeria Religious Freedom and Accountability Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7457
- Origin chamber: House
- Introduced date: 2026-02-10
- Update date: 2026-03-31T08:05:25Z
- Update date including text: 2026-03-31T08:05:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-10: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-10 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-02-10: Introduced in House

## Actions

- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Introduced in House
- 2026-02-10 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-10 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-10",
    "latestAction": {
      "actionDate": "2026-02-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7457",
    "number": "7457",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S000522",
        "district": "4",
        "firstName": "Christopher",
        "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
        "lastName": "Smith",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "Nigeria Religious Freedom and Accountability Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-31T08:05:25Z",
    "updateDateIncludingText": "2026-03-31T08:05:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-10",
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
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-10",
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
          "date": "2026-02-10T15:00:50Z",
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
          "date": "2026-02-10T15:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "M001235",
      "district": "2",
      "firstName": "Riley",
      "fullName": "Rep. Moore, Riley M. [R-WV-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "WV"
    },
    {
      "bioguideId": "M001199",
      "district": "21",
      "firstName": "Brian",
      "fullName": "Rep. Mast, Brian J. [R-FL-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Mast",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "FL"
    },
    {
      "bioguideId": "D000600",
      "district": "26",
      "firstName": "Mario",
      "fullName": "Rep. Diaz-Balart, Mario [R-FL-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Diaz-Balart",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "FL"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "MI"
    },
    {
      "bioguideId": "C001053",
      "district": "4",
      "firstName": "Tom",
      "fullName": "Rep. Cole, Tom [R-OK-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Cole",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "OK"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-03-30",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7457ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7457\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 10, 2026 Mr. Smith of New Jersey (for himself, Mr. Moore of West Virginia , Mr. Mast , Mr. Diaz-Balart , Mr. Huizenga , and Mr. Cole ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require a comprehensive report on United States efforts to address religious persecution and mass atrocities in Nigeria.\n#### 1. Short title\nThis Act may be cited as the Nigeria Religious Freedom and Accountability Act of 2026 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nSystemic religious persecution has persisted in Nigeria since at least 2009, including mass murder, kidnappings, rape, village destruction, and forced displacement of persons, perpetrated by Boko Haram, the Islamic State West Africa Province (ISWAP), Fulani militant groups, and other extremist organizations.\n**(2)**\nEstimates indicate that between 50,000 to 125,000 Christians have been martyred between 2009 and 2025, with more than 19,000 Christian churches attacked or destroyed.\n**(3)**\nFulani-ethnic militias in Nigeria\u2014including networks of armed groups engaged in organized attacks on civilian communities\u2014have carried out repeated acts of violence that meet the statutory definition of terrorist activity under section 212(a)(3) of the Immigration and Nationality Act ( 8 U.S.C. 1182(a)(3) ).\n**(4)**\nThese militias have conducted attacks involving targeted killings, hostage-taking, hijackings, armed assaults, massacres of civilians, destruction of property, and forced displacement of local population.\n**(5)**\nBetween May 2023 and May 2025, Fulani-ethnic militias carried out major massacres in Benue and Plateau States\u2014including attacks in Umogidi, Mgban, Yelwata, the Christmas Eve massacres of 2023 and 2024, and the Holy Week and Easter attacks of 2024 and 2025\u2014killing more than 9,500 people, mostly Christians, and displacing over half a million others.\n**(6)**\nThe acts carried out by these militias are intended to intimidate, coerce, and displace civilian populations, disrupt local governance, and assert control over territory\u2014actions that meet the criteria for designation as a Foreign Terrorist Organization (FTO) under section 219 of the Immigration and Nationality Act ( 8 U.S.C. 1189 ).\n**(7)**\nThe expansion of these militias undermines United States national security and foreign policy interests, destabilizes a strategically important region, jeopardizes religious freedom rights, and exacerbates the threat environment facing West Africa.\n**(8)**\nNigerian Christian clergy and imams who have advocated for tolerance have been kidnapped, tortured, or murdered, with more than 250 religious leaders attacked or killed in the past decade, including Father Sylvester Okechukwu in 2025.\n**(9)**\nChristian leaders such as Father Remigius Iyhula and Bishop Wilfred Anagbe, who testified before Congress in March 2025 and November 2025, have faced intimidation and harassment as a direct result of their testimony regarding the sustained persecution they face.\n**(10)**\nNigeria accounts for 72 percent of all Christians martyred worldwide, according to Open Doors\u2019 2026 Watch List.\n**(11)**\nApproximately 3.5 to 5 million Nigerians are internally displaced, and more than 343,000 remain refugees in the Lake Chad region.\n**(12)**\nIt remains unclear whether any of the limited investigations into these violent attacks have led to prosecutions or convictions of jihadists.\n**(13)**\nDefending oneself from an attack can also lead to a death sentence like in the case of Sunday Jackson, a Christian farmer from Adamawa State, who was sentenced to death in 2021 for the killing of an armed Fulani herder, despite credible evidence that Mr. Jackson acted in self-defense after being violently attacked while working on his farmland.\n**(14)**\nIn a show of good faith from the Nigerian Government, Jackson was pardoned in December 2025 after spending a decade in prison.\n**(15)**\nNigeria retains and enforces blasphemy laws carrying the death penalty in 12 northern states under Sharia criminal law; such laws have been used to target Christians, Muslims, and dissenters.\n**(16)**\nVictims, such as Christians Rhoda Jatau and Deborah Yakubu, have suffered mob violence, imprisonment, or death for alleged blasphemy, while known perpetrators frequently face no punishment.\n**(17)**\nSufi musician Yahaya Sharif-Aminu has been detained for 6 years in Kano State on blasphemy charges and faces the death penalty related to peaceful song lyrics; he is appealing his case to the Supreme Court of Nigeria.\n**(18)**\nThe Nigerian Government routinely denies that religious persecution exists and has failed to adequately intervene, including on early warning notifications of upcoming attacks, including the October 14, 2025, Plateau State massacre.\n**(19)**\nThe United States Commission on International Religious Freedom (USCIRF) has recommended Nigeria\u2019s designation as a Country of Particular Concern (CPC) every year since 2009.\n**(20)**\nIn 2020 and again in October 2025, President Donald J. Trump designated Nigeria a CPC pursuant to the International Religious Freedom Act of 1998 ( 22 U.S.C. 6401 et seq. ).\n**(21)**\nThe prior administration\u2019s removal of Nigeria from the CPC list in 2021 coincided with a marked escalation in religiously motivated violence.\n**(22)**\nDesignating Nigeria as a CPC enhances diplomatic tools\u2014including sanctions\u2014to pressure the Nigerian Government to halt religious persecution, prosecute perpetrators, and protect vulnerable communities.\n#### 3. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nPresident Donald Trump acted justly by designating Nigeria as a Country of Particular Concern, in alignment with the recommendations provided by the United States Commission on International Religious Freedom (USCIRF) and pursuant to the International Religious Freedom Act of 1998 ( 22 U.S.C. 6401 et seq. );\n**(2)**\nthe Government of Nigeria has historically failed to adequately respond to or prevent religiously motivated violence and continues to tolerate impunity by extremist actors, in part by denying the religious nature of such extremism;\n**(3)**\nthe United States should use all available diplomatic, humanitarian, economic, and security tools to pressure the Government of Nigeria to\u2014\n**(A)**\nend impunity for perpetrators of mass atrocities and religious persecution;\n**(B)**\nprotect Christian communities, clergy, and other targeted religious minorities;\n**(C)**\nenable the safe and voluntary return of internally displaced persons to their homelands, prioritizing persecuted Christian communities; and\n**(D)**\nensure freedom of religion is protected by every level of government and that the proper legal channels ensure this right remains wholly intact, including the repeal of blasphemy laws and release prisoners detained for their faith;\n**(4)**\nUnited States Government engagement has encouraged the Nigerian Government to take positive steps towards addressing these threats by extremist groups and are encouraged to engage in a bilateral agreement to protect these vulnerable communities, eliminate jihadist terror activities, further economic cooperation, and counter mutual adversaries in the region;\n**(5)**\nthere is bipartisan congressional support to consider appropriate security cooperation with Nigeria, including conditioning of foreign assistance as was done in the Fiscal Year 2026 National Security, Department of State, and Related Programs Appropriations Bill signed into law by President Trump as part of the Consolidated Appropriations Act, 2026, to enhance efforts to protect innocent lives;\n**(6)**\nthe United States should deliver humanitarian assistance, co-funded by the Government of Nigeria, through trusted civil society organizations, including faith-based organizations, in Nigeria\u2019s middle belt states;\n**(7)**\nthe Department of State and the Department of the Treasury should impose targeted sanctions, including visa bans and asset freezes under the Global Magnitsky Human Rights Accountability Act, on individuals or entities responsible for severe religious freedom violations, or report to Congress the reasons such sanctions have not been imposed, including\u2014\n**(A)**\nFulani-ethnic nomad militias in Nigeria;\n**(B)**\nRabiu Musa Kwankwaso, former Kano State Governor;\n**(C)**\nMiyetti Allah Cattle Breeders Association of Nigeria (MACBAN); and\n**(D)**\nMiyetti Allah Kautal Hore;\n**(8)**\nthe Secretary of State should determine whether certain Fulani-ethnic militias in Nigeria qualify as a foreign terrorist organization under section 219 of the Immigration and Nationality Act ( 8 U.S.C. 1189 );\n**(9)**\nindividuals and networks\u2014domestic or foreign\u2014that provide support to these Fulani-ethnic militias should be investigated and held accountable;\n**(10)**\nthe Secretary of State should consider technical support to the Government of Nigeria to reduce and then eliminate violence from armed Fulani militias, including disarmament programs and comprehensive counter-terrorism cooperation to rid the region of Foreign Terrorist Organizations that pose a direct threat to the American homeland;\n**(11)**\nthe Secretary of State should work with the Government of Nigeria to counteract the hostile foreign exploitation of Chinese illegal mining operations and their destabilizing practice of paying protection money to Fulani militias;\n**(12)**\nthe Nigerian Government should thoroughly investigate instances of penalties or imprisonment under blasphemy laws or Sharia law and work to end these practices and repeal such laws;\n**(13)**\nthe United States stands in solidarity with Christians and all persecuted religious minorities in Nigeria in their right to practice their faith without fear of violence, persecution, or death, and a future goodwill relationship between the United States and Nigeria hinges upon the Nigerian Government\u2019s response moving forward to adequately address the atrocities described in this Act;\n**(14)**\nthe Department of State is encouraged to enlist the support of international partners, including France, Hungary, and the United Kingdom, to work with the Government of Nigeria to promote religious freedom and peace; and\n**(15)**\nthe Government of Nigeria can play a key stabilizing role in the Sahel region and across the continent and is poised to deepen and strengthen their relationship with the United States if they will work with us to combat the persecution of Christians in Nigeria.\n#### 4. Reporting requirement\n##### (a) In general\nNot later than 90 days after the enactment of this Act, and annually thereafter until Nigeria is no longer designated as a Country of Particular Concern pursuant to the International Religious Freedom Act of 1998 ( 22 U.S.C. 6401 et seq. ) and in accordance with the recommendations provided by the United States Commission on International Religious Freedom (USCIRF), the Secretary of State shall submit to the Committee on Foreign Affairs of the House of Representatives, the Committee on Appropriations of the House of Representatives, the Committee on Foreign Relations of the Senate, and the Committee on Appropriations of the Senate a comprehensive report on United States efforts to address religious persecution and mass atrocities in Nigeria.\n##### (b) Elements\nEach report required by subsection (a) shall include the following:\n**(1)**\nAn assessment of Nigeria\u2019s compliance with the International Religious Freedom Act of 1998, including specific actions taken, or not taken, by the Government of Nigeria to prevent persecution, prosecute perpetrators, repeal blasphemy laws, protect vulnerable communities, and facilitate the safe return of internally displaced persons.\n**(2)**\nIdentification of all individuals and entities sanctioned, or under consideration for sanctions, under the Global Magnitsky Human Rights Accountability Act or the Entities of Particular Concern list.\n**(3)**\nA description of co-investments and collaborative efforts between the Government of Nigeria and the United States to provide and deliver humanitarian assistance to Christians displaced by the attacks from Fulani-ethnic militias, through faith-based or nongovernmental partners, including amounts, recipients, type of assistance provided, and measurable outcomes.\n**(4)**\nAn evaluation and description of historical, ongoing, and planned United States security assistance to Nigeria, and a comprehensive assessment of whether such assistance risks enabling or exacerbating religious persecution.\n**(5)**\nWhether the Government of Nigeria is taking appropriate steps to cease enforcement of and repeal blasphemy laws, and to investigate instances of non-Muslims, Muslims, and dissenters being subjected to Sharia law or blasphemy laws.\n**(6)**\nAn assessment of conditions of internally displaced persons, including safety, humanitarian needs, and prospects for return.\n**(7)**\nRecommendations for further executive actions or congressional authority determined to be necessary and most helpful to halt the religious persecution and mass atrocities occurring in Nigeria.\n**(8)**\nAn evaluation of any steps taken by the Government of Nigeria during the reporting period to address religious persecution, dismantle extremist networks, prosecute attackers, reform security forces, or improve protection for at-risk communities.",
      "versionDate": "2026-02-10",
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
        "name": "International Affairs",
        "updateDate": "2026-02-19T18:45:25Z"
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
      "date": "2026-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7457ih.xml"
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
      "title": "Nigeria Religious Freedom and Accountability Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-18T09:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Nigeria Religious Freedom and Accountability Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-18T09:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require a comprehensive report on United States efforts to address religious persecution and mass atrocities in Nigeria.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-18T09:48:26Z"
    }
  ]
}
```
